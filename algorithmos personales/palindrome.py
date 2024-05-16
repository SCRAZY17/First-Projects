""" hello world"""

# algorithme pour détecter les palindrome
SENTENCE = str(
    input("insérer le texte du polindrome ici :")
)  # ejemplo: A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá.
# ejemplo en ruso: Иди, Сеня, не сиди.
# ejemplo en aleman: Ein Neger mit Gazelle zagt im Regen nie.
# ejemplo en inglés : A man, a plan, a canal, Panama!
# ejemplo en chino : 上海自来水来自海上
# el unico lenguaje que no funciona es el arabe
SA = SENTENCE.lower()
S1 = (
    SA.replace("é", "e")
    .replace("ê", "e")
    .replace("è", "e")
    .replace("ë", "e")
    .replace("á", "a")
    .replace("à", "a")
    .replace("â", "a")
    .replace("í", "i")
    .replace("ï", "i")
    .replace("î", "i")
    .replace("ó", "o")
    .replace("ô", "o")
    .replace("ù", "u")
    .replace("ç", "c")
    .replace(" ", "")
    .replace("-", "")
    .replace(".", "")
    .replace("'", "")
    .replace(",", "")
    .replace(":", "")
    .replace("!", "")
    .replace("?", "")
    .replace("(", "")
    .replace(")", "")
    .replace("etc", "")
    .replace(";", "")
)
separated = list(S1)

# mid = len(separated) // 2

# part_1 = "".join(separated[:mid])
# part_2 = separated[mid:]

PART_1 = "".join(separated)
PART_2 = "".join(reversed(PART_1))

if PART_1 == PART_2:
    # print(
    #     "est-il un poin commun entre l'expréssion et son contrère ? :", PART_1 in PART_2
    # )
    print("ce texte forme un palindrome")

else:
    # print(
    #     "est-il un poin commun entre l'expréssion et son contrère ? :", PART_1 in PART_2
    # )
    print("aucun palindrome détecter")
    print("Le texte a l'inverse : " + str(PART_2))


# Define un diccionario de mapeo de caracteres a eliminar
# char_mapping = {
#     "é": "e",
#     "ê": "e",
#     "è": "e",
#     "ë": "e",
#     "á": "a",
#     "à": "a",
#     "â": "a",
#     "í": "i",
#     "ï": "i",
#     "î": "i",
#     "ó": "o",
#     "ô": "o",
#     "ù": "u",
#     "ç": "c",
#     " ": "",
#     "-": "",
#     ".": "",
#     "'": "",
#     ",": "",
#     ":": "",
#     "!": "",
#     "?": "",
#     "(": "",
#     ")": "",
#     "etc": "",
#     ";": "",
# }
