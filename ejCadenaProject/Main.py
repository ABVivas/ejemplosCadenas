#string concatenation
text1 = "Fundamentos con "
text2 = "Python"
result = text1 + text2
print(result)

name = "Angie"
lastName = "Vivas"
fullName = name + " " + lastName
print(fullName)

#format string
price = 97
text3 = f"The price is {price:.2f} dollars"
print(text3)

#math operation
text4 = f"la multiplicación es {20*59} "
print(text4)

#string capitalize
text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

#string casefold()
tittle = "Cien años de Soledad"
tittleConvert = tittle.casefold()
print(tittleConvert)

#string center
fruit = "banana"
texterCenter = fruit.center(20, "-")
print(texterCenter)

#string count
tittle1 = "I love apples, apple are my favorite fruit"
result2 = tittle1.count("apple")
print(result2)

#string endswith
text6= "Curso, fundamentos con Python."
result3 = text6.endswith(".")
print(result3)

#string expandtabs
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#string find
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)

#funcion tittle
text8 = "welcome to my world"
result5 =text8.title()
print(result5)

#funcion isalnum
alphanumeric = "Python312"
result6 =alphanumeric.isalnum()
print(result6)

#funcion isalpha
letters = "Space X"
result7 = letters.isalpha()
print(result7)
