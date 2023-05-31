import re

string1 = "Hola Don Pepito, hola Don José"
string2 = """
								
	
	
	Precio por 1 Kilo :	
	
	





















 




 
 




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 $12.528,20
 
 
 
 



	
	
	
			"""

def busqueda(texto: str) -> list([str]):
    busqueda = re.findall("Kilo.*[\\n \\t]*\$[0-9]+\.?[0-9]*", texto)[0]
    print(busqueda)
    busqueda = re.sub("\W", "", busqueda)
    print(busqueda)
    busqueda = re.findall("[0-9]+\Z", busqueda)[0]
    # busqueda = re.sub("[a-zA-Z\\n \\t]*", "", busqueda[0])
    print(busqueda)
    return busqueda

busqueda(string2)

print(re.findall("(?:Hola|Pepe).*", "Pepeasd"))