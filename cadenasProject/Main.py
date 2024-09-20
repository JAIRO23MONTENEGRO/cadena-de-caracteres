# String Concatenación
"""text = "Fundamentos con "
text2 = "Python"
#text3 = str(5) se convierte para poderlo concatenar, no se concatenan diferentes tippos de datos
result =text + text2
print(result)"""


name ="Andres"
lastName = "Montenegro"
fullName = name + " " + lastName
print(fullName)

# Format String
price = 97
text3 =f"The price is {price:.2f} dollars"
print(text3)

#  Math operation
text4 = f"La multiplicacion es {20 * 59}"
print(text4)

#poner en mayuscula la primera letra de una frase
text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)
#convierte la cadena en minuscula, es mas fuerte que lower()
title = "Cien Años de soledad"
titleConvert = title.casefold()
print(titleConvert)

#pone un caracter en la cadena se deve poner la cantidad y el caracter que se desea poner(20,"-")
fruit = "banana"
textCenter = fruit.center(20,"-")
print(textCenter)

#contar cuantas veces aparece la palabra
title1 = "I love aples, aple are my favorite fruit"
resulit2= title1.count("aple")
print(resulit2)

#String endswith comprueba si dentro de la cadena hay un signo de puntuacion para indicarr que hay termina la cadena

text6 = "Curso, fundamentos conPython."
result3 = text6.endswith(".")
print(result3)

# String expandtabs tabular
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#String find() encuentra la primera palabra que coincide, da la cantidad de caracteres que existen antes de
text7 = "Hola, bienvenidos a colombia."
result4 = text7.find("bienvenidos")
print(result4)

#Funcion title pone cada primera palabra del titulo en mayuscula
text8 = "wlcome to my word"
result5 = text8.title()
print(result5)

#Funclion isalum devuelve verdadero si la cadena es alfanumerica
alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)

#Funcion isalpha
letters = "Space x"
result7 =letters.isalpha()
print(result7)