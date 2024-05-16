"""
HELLO WORLD
"""

import math

print("ex11:")

num = int(input("insérer un nombre entier pour le calcule factoriel:"))

RESULTAT = 1
for i in range(1, num + 1):
    RESULTAT *= i

print(f"le factoriel de {num} est: {RESULTAT}")

n = int(input("n ="))
factorial_de_n = math.factorial(n)
print(f"Le factoriel de {n} est: {factorial_de_n}")

N1 = int(input("N1 ="))

FACT = 1
C = 1
while C < N1 + 1:
    FACT *= C
    C += 1
print("N =", FACT)
