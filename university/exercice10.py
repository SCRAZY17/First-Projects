"""
Programme pour calculer, la somme des nombres entiers paires
"""

N = int(input("Introduir un nombre entier pour votre calcule: "))

SOMME_PAIRES = 0
for i in range(N, 0, -1):
    if i % 2 == 0:
        SOMME_PAIRES += i

print(f"La somme des nombres paires entre {N} et 1 est: {SOMME_PAIRES}")
