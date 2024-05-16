"""HELLO WORLD"""

N = int(input("N="))
N1 = N
SOMME = 0
while N > 0:
    SOMME += N
    N -= 1
print(f"La somme des nombres entiers entre 0 et {N1} est: {SOMME} ")


START = 0
N2 = int(input("insérer un nombre  : "))

SOMME = sum(range(START, N2 + 1))

print(f"La somme entre les nombres entiers {START} et {N2} est: {SOMME}")
