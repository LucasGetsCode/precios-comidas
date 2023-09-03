url_carrefour: str = 'https://www.carrefour.com.ar/bebidas/gaseosas/gaseosas-cola?fuzzy=0&map=category-1,category-2,category-3,brand&operator=and&order=&page=1&query=/bebidas/gaseosas/gaseosas-cola/coca-cola' 
url_coto: str = "https://www.cotodigital3.com.ar/sitios/cdigi/browse?_dyncharset=utf-8&Dy=1&Ntt=coca+cola&Nty=1&Ntk=&siteScope=ok&_D%3AsiteScope=+&atg_store_searchInput=coca+cola&idSucursal=200&_D%3AidSucursal=+&search=Ir&_D%3Asearch=+&_DARGS=%2Fsitios%2Fcartridges%2FSearchBox%2FSearchBox.jsp"
url_dia: str = "https://diaonline.supermercadosdia.com.ar/coca%20cola?page=1"
limite: int = 16
debug: int = 1
message: str = "Oops, se nos acabó el tiempo"
precios_totales: list([int]) = []
articulos_totales: int = 0

#importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import statistics
import re

options = webdriver.ChromeOptions() 
options.headless = True # Si no carga puede que sea por esto

# options.add_argument('user-agent=fake-useragent')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36") # Evita algunos errores
options.add_argument("--log-level=3") # Evita que se vean los mensajes de la consola de la página (errores, info, etc que no importan)
# options.add_argument("--enable-javascript")
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')

def wait_seconds(segundos: int, repetira: bool=False, debug:int=0):
	if debug > 1:
		if repetira == False:
			print(f"Ya se cargó un elemento, esperando {segundos} mientras se terminan de cargar.")
		else:
			print(f"Ya se cargó el primero, esperando {segundos} segundos para repetir.")
	for i in range(segundos):
		time.sleep(1)
		if debug > 1: print(segundos-1-i)

def print_promedios(precios: list, seleccion:str="todos"):
	sel: str = seleccion.lower()
	if len(precios) != 0:
		print(sorted(precios))
		promedio = statistics.mean(precios)
		median = statistics.median(precios) # Quedarse con este
		median_grouped = statistics.median_grouped(precios)
		median_low = statistics.median_low(precios)
		if sel == "todos":
			print("Mean: $" + str(round(promedio,2)))
			print("Median: $" + str(round(median,2)))
			print("Median Grouped: $" + str(round(median_grouped,2)))
			print("Median Low: $" + str(round(median_low,2)))
		if sel == "mean":
			print("Mean: $" + str(round(promedio,2)))
		if sel == "median":
			print("Median: $" + str(round(median,2)))


def carrefour_busqueda(driver, url, limite=16, debug:int=0):
	# clase = 'lyracons-dynamic-weight-price-0-x-currencyContainer'
	clase_container = "valtech-carrefourar-dynamic-weight-price-0-x-currencyContainer" # Puede que vayan cambiando los nombres de la clase
	clase_precio = "valtech-carrefourar-dynamic-weight-price-0-x-currencyInteger"
	precios = []
	driver.get(url)          #open the URL
	driver.implicitly_wait(15) #maximum time to load the link
	if debug > 0: print("Página cargada, esperando a que carguen los artículos de CARREFOUR")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)") # Mueve la ventana para que se carguen bien los elementos

	email = WebDriverWait(driver, 30, ignored_exceptions=[TimeoutException]).until(EC.visibility_of_element_located((By.CLASS_NAME, clase_container)), message=message)
	wait_seconds(2, repetira=True, debug=debug) # Está repetido porque por alguna razón desaparece al encontrarlo por primera vez

	email = WebDriverWait(driver, 30, ignored_exceptions=[TimeoutException]).until(EC.visibility_of_element_located((By.CLASS_NAME, clase_container)), message=message)
	wait_seconds(3, debug=debug) # Aunque aparezca uno puede que el resto no, entonces le doy un tiempo para que cargue
	if debug > 0: print("Productos cargados")
	result = driver.page_source
	soup = BeautifulSoup(result, 'html.parser')
	page = list(soup.findAll('span', class_=clase_container)) # Span del tipo $ 512,32, separado -$- -512-,-32-
	for span in range(min(limite, len(page))):
		# print(span.text)
		precios.append(int(page[span].find('span', class_=clase_precio).text)) # Span de tipo entero
	if debug > 1: print_promedios(precios, "median")
	if debug > 1: print(f"{len(page)} artículos encontrados")
	if debug > 0: print("Listo (carrefour)")
	global precios_totales, articulos_totales
	precios_totales += precios
	articulos_totales += len(page)

def coto_busqueda(driver, url, limite=16, debug:int=0):
	clase = "unit"
	precios = []
	driver.get(url)          #open the URL
	driver.implicitly_wait(15) #maximum time to load the link
	if debug > 0: print("Página cargada, esperando a que carguen los artículos de COTO")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)") # Mueve la ventana para que se carguen bien los elementos

	email = WebDriverWait(driver, 30, ignored_exceptions=[TimeoutException]).until(EC.visibility_of_element_located((By.CLASS_NAME, clase)), message=message)
	wait_seconds(1, debug=debug) # Por las dudas más que nada
	if debug > 0: print("Productos cargados")
	result = driver.page_source
	soup = BeautifulSoup(result, 'html.parser')
	page = list(soup.findAll('span', class_=clase)) # Span del tipo $ 512,32, separado -$- -512-,-32-
	for span in range(min(limite, len(page))):
		# print(page[span].text.replace("\n", "").replace("\t", "").replace("  ", ""))
		precios.append(int(re.search("[0-9]+[0-9]+\.?[0-9]*", page[span].text).group())) # Span de tipo entero
	if debug > 1: print_promedios(precios, "median")
	if debug > 1: print(f"{len(page)} artículos encontrados")
	if debug > 0: print("Listo (coto)")	
	global precios_totales, articulos_totales
	precios_totales += precios
	articulos_totales += len(page)


def dia_busqueda(driver, url, limite:int=16, debug:int= 0):
	clase = "vtex-product-specifications-1-x-specificationValue"
	precios = []
	driver.get(url)          #open the URL
	driver.implicitly_wait(15) #maximum time to load the link
	if debug > 0: print("Página cargada, esperando a que carguen los artículos de DIA")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)") # Mueve la ventana para que se carguen bien los elementos

	email = WebDriverWait(driver, 30, ignored_exceptions=[TimeoutException]).until(EC.visibility_of_element_located((By.CLASS_NAME, clase)), message=message)
	wait_seconds(3, debug=debug) # Por las dudas más que nada
	# email = WebDriverWait(driver, 30, ignored_exceptions=[TimeoutException]).until(EC.visibility_of_element_located((By.CLASS_NAME, clase)), message=message)
	# wait_seconds(3)
	if debug > 0: print("Productos cargados")
	result = driver.page_source
	soup = BeautifulSoup(result, 'html.parser')
	page = list(soup.findAll('span', class_=clase)) # Span del tipo $ 512,32, separado -$- -512-,-32-
	for span in range(min(limite*2, len(page))):
		# print(page[span].text)
		if "." in page[span].text:
			precios.append(float(re.search("[0-9]+[0-9]+\.?[0-9]*", page[span].text).group())) # Span de tipo entero
	if debug > 1: print_promedios(precios, "median")
	if debug > 1: print(f"{len(page)/2} artículos encontrados")
	if debug > 0: print("Listo (dia)")
	global precios_totales, articulos_totales
	precios_totales += precios
	articulos_totales += int(len(page)/2)


with webdriver.Chrome('chromedriver', options=options) as driver:
	carrefour_busqueda(driver, url_carrefour, limite, debug=debug)
	coto_busqueda(driver,url_coto, limite, debug=debug)
	dia_busqueda(driver, url_dia, limite, debug=debug)
	print_promedios(precios_totales)
	print(articulos_totales)

	# driver.maximize_window() #maximize the window
	# driver.set_window_size(1024, 768)
	# driver.set_window_position(0, 0) # Top left