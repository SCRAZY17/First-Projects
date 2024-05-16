import math

print("ex06:")


# "we have X=variable, if X < 0, result = X*(-1). if X>=0, result = X. print the result"
x = float(input("X="))

print(
    "Result X=", math.fabs(x)
)  # la funcion "abs" devuelve el valor absoluto de tu numero
print("Result X=", abs(x))
# usar abs es mejor porque tiene una mejor tolerancia con numeros complejos y es capaz de identificar numeros enteros.
