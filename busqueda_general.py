url = 'https://www.carrefour.com.ar/bebidas/gaseosas/gaseosas-cola?fuzzy=0&map=category-1,category-2,category-3,brand&operator=and&order=&page=1&query=/bebidas/gaseosas/gaseosas-cola/coca-cola' 
clase = 'lyracons-dynamic-weight-price-0-x-currencyContainer'

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

options = webdriver.ChromeOptions() 
options.headless = True # Si no carga puede que sea por esto

# options.add_argument('user-agent=fake-useragent')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36") # Evita algunos errores
options.add_argument("--log-level=3") # Evita que se vean los mensajes de la consola de la página (errores, info, etc que no importan)
# options.add_argument("--enable-javascript")
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
with webdriver.Chrome('chromedriver', options=options) as driver:

	# url = 'https://www.doordash.com/en-US'
	# driver.maximize_window() #maximize the window
	# driver.set_window_size(1024, 768)
	# driver.set_window_position(0, 0) # Top left
	driver.get(url)          #open the URL
	driver.implicitly_wait(15) #maximum time to load the link
	print("Página cargada, esperando a que carguen los artículos")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)") # Mueve la ventana para que se carguen bien los elementos

	message = "Oops, se nos acabó el tiempo"
	email = WebDriverWait(driver, 30, ignored_exceptions=[TimeoutException]).until(EC.visibility_of_element_located((By.CLASS_NAME, clase)), message=message)
	segundos = 2
	print(f"Ya se cargó el primero, esperando {segundos} segundos para repetir")
	for i in range(segundos):
		time.sleep(1)
		print(segundos-1-i) # Está repetido porque por alguna razón desaparece al encontrarlo por primera vez

	email = WebDriverWait(driver, 30, ignored_exceptions=[TimeoutException]).until(EC.visibility_of_element_located((By.CLASS_NAME, clase)), message=message)
	segundos = 3
	print(f"Ya se volvió a cargar uno, esperando {segundos} segundos")
	for i in range(segundos):
		time.sleep(1)
		print(segundos-1-i) # Aunque aparezca uno puede que el resto no, entonces le doy un tiempo para que cargue
	print("Productos cargados")
	result = driver.page_source
	soup = BeautifulSoup(result, 'html.parser')
	page = list(soup.findAll('span', class_=clase)) # Span del tipo $ 512,32, separado -$- -512-,-32-
	precios = []
	for span in page:
		print(span.text)
		precios.append(int(span.find('span', class_="lyracons-dynamic-weight-price-0-x-currencyInteger").text)) # Span de tipo entero
	if len(precios) != 0:
		print(precios.sort())
		promedio = statistics.mean(precios)
		median = statistics.median(precios) # Quedarse con este
		median_grouped = statistics.median_grouped(precios)
		median_low = statistics.median_low(precios)
		print("Mean: $" + str(round(promedio,2)))
		print("Median: $" + str(round(median,2)))
		print("Median Grouped: $" + str(round(median_grouped,2)))
		print("Median Low: $" + str(round(median_low,2)))
	print(f"{len(page)} artículos encontrados")
	print("Listo")
	# driver.quit()