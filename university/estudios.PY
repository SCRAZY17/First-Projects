# print(
#     """
# Practicando en Python
# """
# )

# puedes multiplicar un string en un print para que se imprima en la terminal multiples veces.
# para escribir un string de varias lineas se utiliza """"""
# la funcion de len puede ensenarte la longitud de otra funcion por ejemplo----->
# saludo = "hola"
# burla = "eres un gallina!!!"
# print("el numero de caracteres del texto es:", len(saludo))
# print(burla[0:5])
# saludo_burlon = f"{saludo} {", "} {burla}"
# print(saludo_burlon.upper())
# print(
#     saludo_burlon.strip().capitalize()
# )  # esto coje solo el primer caracter del string y lo pone en majuscula,
# # importante: esto no detecta palabra isa que si ay un espacio en el principio del string no se mostrara ningun caracter en majuscula,
# # por eso anadi un strip ANTES del metodo 'capitalize' y eso se llama encadenar
# print(
#     saludo_burlon.title() * 4
# )  # esto coje solo el primer caracter de cada palabra y lo pone en majuscula el resto se queda en minusculas
# print(saludo_burlon.find("gallina"))
# print(saludo_burlon.find("2"))  # aqui va a imprimir -1 ya que no lo encuentra
# print(
#     saludo_burlon.replace(saludo_burlon[17:], '"buen amigo"')
# )  # este back slash hace python no considere a las comillas dobles como una funsion
# print("hola" in saludo_burlon)
# print("amigo" not in saludo_burlon)
# print("hello \nWorld")
