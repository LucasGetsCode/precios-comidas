import aiohttp
import asyncio
import re
import time
from bs4 import BeautifulSoup

import importar_links

links = importar_links.obtener_links("precios_ingredientes.xlsx")

# coto_url: str = "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-original-nescafe-fra-100-grm/_/A-00522410-00522410-200"
# coto_url2: str = "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-sabor-original--3-lt/_/A-00102153-00102153-200"
# dia_url: str = "https://diaonline.supermercadosdia.com.ar/agua-saborizada-levite-naranja-225-lts-116178/p"
# dia_url2: str = "https://diaonline.supermercadosdia.com.ar/nescafe-dolca-original-ideal-para-batir-170-gr-171360/p"
# carrefour_url: str = "https://www.carrefour.com.ar/cafe-instantaneo-nescafe-tradicion-frasco-170-g-582553/p"
# carrefour_url2: str = "https://www.carrefour.com.ar/gaseosa-7-up-light-lima-limon-225-l/p"
# carrefour_url3: str = "https://www.carrefour.com.ar/gaseosa-coca-cola-zero-175-l-636689/p"
# carrefour_url4: str = "https://www.carrefour.com.ar/leche-parcialmente-descremada-fresca-la-serenisima-sachet/p"
# coto_lista_url: list([str]) = [coto_url,coto_url2]
# dia_lista_url: list([str]) = [dia_url,dia_url2]
# carrefour_lista_url: list([str]) = [carrefour_url,carrefour_url2,carrefour_url3,carrefour_url4]


def normalizar(precio, cantidad, unidad):
    if unidad.lower() in ["kg", "k", "l", "kilo", "litro", "kilogramo"]:
        precio_por_mil = float(precio) / float(cantidad)
    else:
        precio_por_mil = 1000 * float(precio) / float(cantidad)
    return precio_por_mil

def promedio_unidades(total_unidades: list([str])) -> str:
    kilos: int = 0
    litros: int = 0
    for unidad in total_unidades:
        if unidad == "kilo": kilos += 1
        elif unidad == "litro": litros +=1
    return "kilo" if kilos >= litros else "litro"
    

def coto(page):
    precio = re.search("(?:Kilo|Litro).*[\\n \\t]*\$[0-9]+\.?[0-9]*", page.text).group()
    precio = re.sub("\W", "", precio)
    unidades = "kilo" if "Kilo" in precio else "litro"
    precio = re.search("[0-9]+\Z", precio).group()
    # print(f"Precio por {unidades}: ${precio}")
    return (int(precio), unidades)

def dia(page):
    precio = page.find_all("span", class_="vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last")
    unidades = "kilo" if "KG" in precio[1] else "litro"
    precio = precio[0].text.split(".")[0]
    # print(f"Precio por {unidades}: ${precio}")
    return (int(precio), unidades)

def carrefour(page):
    precio = page.find_all("span", class_="valtech-carrefourar-product-price-0-x-currencyContainer")[-1]
    precio = re.search("[0-9]+\.?[0-9]*", precio.text).group()
    cantidad = page.find("span", class_="vtex-store-components-3-x-productBrand vtex-store-components-3-x-productBrand--quickview")
    cantidad = re.search("[0-9]+\.?[0-9]* (?:l|g|k)", cantidad.text)
    cantidad = cantidad.group().split(" ") if cantidad != None else [1,"l"]
    precio = int(normalizar(precio, cantidad[0], cantidad[1]))
    unidades = "kilo" if ("k" in cantidad[1] or "g" in cantidad[1]) else "litro"
    # print(f"Precio por {unidades}: ${precio}")
    return (int(precio), unidades)

def coto_busqueda(page):
    pass

def dia_busqueda(page):
    pass

def carrefour_busqueda(page):
    pass

    
async def fetch(session, url):
    async with session.get(url) as response:
        # return await response.text()
        return await response.read()

async def main():
    inicio = time.time()
    async with aiohttp.ClientSession() as session:
        for ingrediente in links.values():
            for url in ingrediente["links_coto"]:
                ingrediente["html_coto"].append(await fetch(session, url))
            for url in ingrediente["links_dia"]:
                ingrediente["html_dia"].append(await fetch(session, url))
            for url in ingrediente["links_carrefour"]:
                ingrediente["html_carrefour"].append(await fetch(session, url))
                
    for ingrediente in links.values():
        for html in ingrediente["html_coto"]:
            resultados = coto(BeautifulSoup(html.decode('utf-8'), 'html.parser'))
            ingrediente["precios"].append(resultados[0])
            ingrediente["unidades"].append(resultados[1])
        for html in ingrediente["html_dia"]:
            resultados = dia(BeautifulSoup(html.decode('utf-8'), 'html.parser'))
            ingrediente["precios"].append(resultados[0])
            ingrediente["unidades"].append(resultados[1])
        for html in ingrediente["html_carrefour"]:
            resultados = carrefour(BeautifulSoup(html.decode('utf-8'), 'html.parser'))
            ingrediente["precios"].append(resultados[0])
            ingrediente["unidades"].append(resultados[1])        
        ingrediente["precio"] = (sum(ingrediente["precios"])/len(ingrediente["precios"]))
        unidades = promedio_unidades(ingrediente["unidades"])
        print(f"{ingrediente['nombre'].capitalize()}: ${ingrediente['precio']} / {'kg' if unidades == 'kilo' else 'l'}")

    print("Tiempo total: " + str(round(time.time() - inicio, 3)))

loop = asyncio.get_event_loop()
pagina = loop.run_until_complete(main())
