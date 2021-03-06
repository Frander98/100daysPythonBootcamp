# ----------TIPOS DE ERRORES MAS COMUNES----------#
""""Se presenta el error tipo FileNotFoundError y luego se muestra
una manera de manejar la excepci贸n."""
# FileNotFoundError 馃憞
# with open("file.txt") as file:
#     file.read()
"""En el siguiente bloque de c贸digo, el int茅rprete trata de abrir un archivo de texto
pero no lo encuentra ya que no existe, luego, por medio de la excepci贸n se le da una 
alternativa al int茅rprete, en este caso se le indica que cree un archivo nuevo con el
nombre indicado. De esta manera el programa no se cae estrepitosamente"""
# try:
#     file = open("file.txt", "r")
# except FileNotFoundError:
#     file = open("file.txt", "w")
# ----------**********----------

""""Se presenta el error tipo KeyError y luego se muestra
una manera de manejar la excepci贸n."""
# KeyError 馃憞
# dict = {"Costa Rica": "San Jos茅", "Honduras": "Tegucigalpa"}
# capital = dict["USA"]
"""En el siguiente bloque de c贸digo, el int茅rprete intenta acceder a un valor del diccionario
por medio de una llave, pero al no existir dicha llave, arroja una excepcion que permite crear 
dicha llave y asignarle un valor."""
# try:
#     diction = {"Costa Rica": "San Jos茅", "Honduras": "Tegucigalpa"}
#     capital = diction["USA"]
# except KeyError:
#     diction["USA"] = "Washington"
#     print(diction)
# ----------**********----------

"""Se presenta el error tipo IndexError y luego se muestra una manera de manejar la 
excepcion."""
# IndexError 馃憞
# fruits = ['apple', 'banana', 'strawberry']
# print(fruits[3])
"""En el siguiente bloque de c贸digo, el interprete trata de buscar un indice dentro de una lista, pero
dicho indice excede la longitud de la lista y arroja una excepcion en la que agrega al final de la lista 
un nuevo elemento y luego tratar de acceder a su indice."""
# try:
#     fruits = ['apple', 'banana', 'strawberry']
#     print(fruits[3])
# except IndexError:
#     fruits.append("pineapple")
#     print(fruits[3])
# ----------**********----------

"""Se presenta el error tipo TypeError y luego se muestra una manera de manejar la 
excepcion."""
# TypeError 馃憞
# text = "Hello World!"
# print(text + 10)
"""En el siguiente bloque de c贸digo, el interprete no puede manejar la concatenacion de 
dos valores de tipos distintos, por lo cual en la excepcion se convierte el valor numerico
a un valor tipo String para concatenarlo correctamente."""
# try:
#     text = "Hello World! "
#     print(text + 10)
# except TypeError:
#     print(text + "10")


# ----------SINTAXIS EN PYTHON PARA EL MANEJO DE EXCEPCIONES----------#
# try --> Algo que podr铆a causar una excepcion
# except --> Hacer lo que est谩 en este bloque en caso de que haya habido una excepcion.Se pueden crear varias
#excepciones, como en el siguiente ejemplo que hay 2 sentencias except:
# try:
#     pass
# except:
#     pass
# except:
#     pass
# except:
#     pass
# finally:
#     pass
# else --> Hacer lo que est谩 en este bloque en caso de que NO hayan habido excepciones.
# finally -->Hacer lo que est谩 en este bloque tanto si hubo como si no hubo excepciones.

#Levantar excepciones propias
"""Se pueden crear excepciones propias con la palabra raise, esto sirve para cuando el codigo es
perfectamente v谩lido (es decir va a correr) pero levantamos una excepcion en caso de considerarlo pertinente.
Para hacerlo ocupamos indicarle el tipo de error, para esto usamos algun tipo de excepcion conocida, como las listadas
al principio de este archivo u otros provistos por el lenguaje."""
# Ejemplo de uso de la palabra raise
"""El siguiente es un programa para calcular el indice de masa corporal. La altura maxima que le permitimos al 
usuario ingresar no puede exceder los 3 metros(ning煤n humano mide m谩s que eso)"""
# height = float(input("Ingrese su altura: "))
# weight = int(input("Ingrese su peso: "))
# if height > 3:
#     raise ValueError
# else:
#     bmi = weight / (height**2)
#     print("Su IMC es ", bmi)
