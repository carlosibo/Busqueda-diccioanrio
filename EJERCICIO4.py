#Creado por Carlos Andres Iborra Alvarez
LETRAS = "AEIMORTVY" #letrascontenidasenlapalabraquebuscamos
fichero = open('/Users/carlos/Desktop/nombres_mujer.txt','r') #Diccionariousado
contenido = ""
x=1

while contenido != "ROBERTOXX": #Palabra final diccioanrio
	contenido = fichero.readline(x)
	contenido = contenido.upper()
	contenido = contenido.rstrip()
	imprimir = True #El if de abajo criterios de busqueda
	if (len(contenido) == 5) and (contenido[3] =="T") and (contenido[0]== "M"):
		for letra in contenido:
			if LETRAS.find(letra) == -1:
				imprimir = False
		if imprimir == True:
			print contenido
	x=x+1

x=1
print "FIN"
