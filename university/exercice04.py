print("ex04:")
N1 = float(input("note 1="))
N2 = float(input("note 2="))
N3 = float(input("note 3="))
C1 = int(2)
C2 = int(3)
C3 = int(1)

S = float((N1 * C1) + (N2 * C2) + (N3 * C3))
print("somme =", S)

M = float(S / (C1 + C2 + C3))
print("La moyenne=", M)
print("M int =", round(M))
