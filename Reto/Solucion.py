
import re
texto="En la maratón número 12, el corredor llamado \"Carlos\" completó la carrera en 3.75 horas, registrando tiempos parciales en kilómetros [5, 10, 15, 20, 25, 30, 35, 40] minutos; aunque estaba fatigado, su condición física estaba óptima y logró mantener el ritmo constante gracias a que el entrenamiento previo fue exitoso."
patron1 = r"-?\b\d+\b"
patron2 = r"-?\b\d+\.\d+\b"
patron3 = r"\b(True|False)\b"
patron4 = r'"(.*?)"'
patron5 = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
enteros = re.findall(patron1, texto)
flotantes = re.findall(patron2, texto)
booleans = re.findall(patron3, texto, re.IGNORECASE)
strings = re.findall(patron4, texto)
listas = re.findall(patron5, texto,)
print ()
print("El texto es: ",texto)
print()
print("Los enteros son: ",enteros)
print("La cantidad de enteros es de: ",len(enteros))
print("Los flotantes son: ",flotantes)
print("La cantidad de flotantes es de: ",len(flotantes))
print("Los booleans son: ",booleans)
print("La cantidad de booleans son de: ",len(booleans))
print("Los strings son: ",strings)
print("La cantidad de strings es de: ",len(strings))
print("Las listas son: ",listas)
print("La cantidad de listas son de: ",len(listas))
texto1=input("Ingrese su texto: ")
enteros = re.findall(patron1, texto1)
flotantes = re.findall(patron2, texto1)
booleans = re.findall(patron3, texto1, re.IGNORECASE)
strings = re.findall(patron4, texto1)
listas = re.findall(patron5, texto1)
print ()
print("El texto es: ",texto)
print()
print("Los enteros son: ",enteros)
print("La cantidad de enteros es de: ",len(enteros))
print("Los flotantes son: ",flotantes)
print("La cantidad de flotantes es de: ",len(flotantes))
print("Los booleans son: ",booleans)
print("La cantidad de booleans son de: ",len(booleans))
print("Los strings son: ",strings)
print("La cantidad de strings es de: ",len(strings))
print("Las listas son: ",listas)
print("La cantidad de strings son de: ",len(strings))












