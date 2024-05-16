print("ex07:")

T = float(input("Température="))
if T < 0:
    print("Il gèle")
elif 0 <= T <= 35:
    print("Bon climat")
elif T > 35:
    print("Alerte à la canicule")
