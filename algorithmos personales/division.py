"""hello world"""

from datetime import date

# un algorithmo para dividir sin la utilizacion del signo / o *

print("date of execution : " + str(date.today()))

num1 = float(input("premier nombre ="))
num2 = float(input("deuxième nombre ="))
num0 = num1
neg_num1 = abs(num1)
neg_num2 = abs(num2)

REQUEST = int(
    input(
        """Voulez vous un résultat entier où réel? 
        pour un résultat entier ensérer : 1; pour un résultat réel insérer : 2
        écrire votre pétition ici------->"""
    )
)

RESULTADO = None  # se determina un resultado sin valor
if num2 > 0 and num1 >= 0:
    RESULTADO = 0
    while num1 >= num2:
        num1 -= num2  # esto significa : num1 = num1 - num2
        RESULTADO += 1
# para los numeros negativos
elif num1 < 0 and num2 < 0:  # esto tiene que ejecutarse antes quel sigiente elif
    RESULTADO = 0
    while neg_num1 >= neg_num2:
        neg_num1 -= neg_num2
        RESULTADO += 1
elif num2 < 0 or num1 < 0:
    RESULTADO = 0
    while neg_num1 >= neg_num2:
        neg_num1 -= neg_num2
        RESULTADO -= 1
CALC = 0
for _ in range(abs(RESULTADO)):
    CALC += num2 if RESULTADO > 0 else -num2
if RESULTADO is not None and REQUEST == 1:
    print(f"Le résultat est: {RESULTADO}")
    # Reemplazar la multiplicación

    if (CALC - num0) != 0:
        print("Le reste est : " + str(num0 - CALC))
    else:
        print("il ne reste rien")
elif RESULTADO is None:
    print("erreur")
RESTO = num0 - CALC
# operacion hecha para un resultado de valor entero
if REQUEST == 2:
    Q = int(
        input(
            """sélectioner un grade de précision en écrevent le nombre des chifres après la vergule,
            ce système a une précision maximale de 4 chifres avant d' attiendre l'infinie;
                pour sélectioner l'infinie insérer 99: """
        )
    )
    if Q == 0:
        B = 0
    elif Q == 1:
        B = 10
    elif Q == 2:
        B = 100
    elif Q == 3:
        B = 1000
    elif Q == 4:
        B = 10000
    elif Q == 99:
        B = 1000000000000000000000
    else:
        Q1 = int(
            input(
                """La valeur insérer est invalide, s'il vous plais réinsérer votre valeur: """
            )
        )

        if Q1 == 0:
            B = 0
        elif Q1 == 1:
            B = 10
        elif Q1 == 2:
            B = 100
        elif Q1 == 3:
            B = 1000
        elif Q1 == 4:
            B = 10000
        elif Q1 == 99:
            B = 100000000000000000
        # else:
        #     print("VETE DE AQUI!!!")
    print(
        """
    si la valeur avec des nombres après la virgule est infinie
      le programme peut prendre un long temp 
    """
    )
    RESTO_1 = 0
    for _ in range(abs(B)):
        RESTO_1 += RESTO if B > 0 else -RESTO
    REP_num02 = num2  # num2
    REV_RESTO_1 = abs(RESTO_1)
    REV_REP_num02 = abs(REP_num02)

    RESULT = None  # se determina un resultado sin valor
    if REP_num02 > 0 and RESTO_1 >= 0:
        RESULT = 0
        while RESTO_1 >= REP_num02:
            RESTO_1 -= REP_num02  # esto significa : num1 = num1 - num2
            RESULT += 1
    # para los numeros negativos
    elif RESTO_1 < 0 and REP_num02 < 0:
        RESULT = 0
        while REV_RESTO_1 >= REV_REP_num02:
            REV_RESTO_1 -= REV_REP_num02
            RESULT += 1
    elif REV_RESTO_1 < 0 or RESTO_1 < 0:
        RESULT = 0
        while REV_RESTO_1 >= REV_REP_num02:
            REV_RESTO_1 -= REV_REP_num02
            RESULT -= 1
    if RESULT is not None:
        print(f"le résultat en nombres réels est: {RESULTADO}, {RESULT}")
