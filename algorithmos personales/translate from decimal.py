# a = "u"
# (
#     a + "zekdzl"
# )  # no puedes añadirle un valor a tu cadena ya que las cadenas son inmutables pero al contrario puedes cambiarles de valor
# print(a)
# \n :este caracter salta de linea en strings de multiples lineas.

# importante!!! : if you're looking to find an explicit data on a long string you need to separe every separated data using the "split" element,
# then depending on the type of the data you call it using print()
# muy importante si quieres llamar a un numero usando-----> if -4 .isnumeric : print(true) else : print(false)
# te devolvera false ya que python considera el signo "-" como un gion no un numero
# asi que deberias usar el valor absoluto o if -4 .startswith ("-") : print(true)


# moon_facts = [
#     "The Moon is drifting away from the Earth.",
#     "On average, the Moon is moving about 4cm every year.",
# ]
# print(" ".join(moon_facts))
# print(moon_facts) # descomenta todo esto para saber que hace el .join


# esto es la manera de encontrar una expresion especifica en un str largo------------>
# text = """Interesting facts about the Moon. The Moon is Earth's only satellite.
# There are several interesting facts about the Moon and how it affects life here on Earth.
# On average, the Moon moves 4cm away from the Earth every year.
# This yearly drift is not significant enough to cause immediate effects on Earth.
# The highest daylight temperature of the Moon is 127 C."""
# s = text.split(". ")
# print(s)
# for se in s:
#     if "temperature" in se:
#         print(se)


import sys
from datetime import date

na = int(input("your number: "))
n8 = na
nh = na
num = str(na)
binario = ""
while na > 0:
    residuo = na % 2
    binario = str(residuo) + binario
    na = na // 2
print(f"the number in binary: {int(binario)}")

# oct = ""
# while n8 > 0:
#     residu = n8 % 8
#     oct = str(residu) + oct
#     n8 = n8 // 8
# print(f"the number in octal: {int(oct)}")
HEX = ""
while nh > 0:
    resid = nh % 16
    if resid == 10:
        resid = "A"
    elif resid == 11:
        resid = "B"
    elif resid == 12:
        resid = "C"
    elif resid == 13:
        resid = "D"
    elif resid == 14:
        resid = "E"
    elif resid == 15:
        resid = "F"
    HEX = str(resid) + HEX
    nh = nh // 16
print(f"the number in hexadecimal: {HEX}")

# print(len(num), len(binario), len(oct), len(hex))

num_X = str(binario)

num_1 = num_X.replace("0", "")
num_1 = len(num_1)

num_2 = num_X.replace("1", "")
num_2 = len(num_2)

if num_1 == num_2 + 1:
    print(f"the number {num} is a perfect number.")

HEX = "".join(reversed(HEX))
a = None
b = None
c = None
d = None
e = None
f = None
g = None
h = None
i = None
a = HEX[0]
if a == "A":
    a = 10
elif a == "B":
    a = 11
elif a == "C":
    a = 12
elif a == "D":
    a = 13
elif a == "E":
    a = 14
elif a == "F":
    a = 15
a = int(a)
if len(HEX) > 1:
    b = HEX[1]
    if b == "A":
        b = 10
    elif b == "B":
        b = 11
    elif b == "C":
        b = 12
    elif b == "D":
        b = 13
    elif b == "E":
        b = 14
    elif b == "F":
        b = 15
b = int(b)

if len(HEX) > 2:
    c = HEX[2]
    if c == "A":
        c = 10
    elif c == "B":
        c = 11
    elif c == "C":
        c = 12
    elif c == "D":
        c = 13
    elif c == "E":
        c = 14
    elif c == "F":
        c = 15
    c = int(c)
if len(HEX) > 3:
    d = HEX[3]
    if d == "A":
        d = 10
    elif d == "B":
        d = 11
    elif d == "C":
        d = 12
    elif d == "D":
        d = 13
    elif d == "E":
        d = 14
    elif d == "F":
        d = 15
    d = int(d)
if len(HEX) > 4:
    e = HEX[4]
    if e == "A":
        e = 10
    elif e == "B":
        e = 11
    elif e == "C":
        e = 12
    elif e == "D":
        e = 13
    elif e == "E":
        e = 14
    elif e == "F":
        e = 15
    e = int(e)
if len(HEX) > 5:
    f = HEX[5]
    if f == "A":
        f = 10
    elif f == "B":
        f = 11
    elif f == "C":
        f = 12
    elif f == "D":
        f = 13
    elif f == "E":
        f = 14
    elif f == "F":
        f = 15
    f = int(f)
if len(HEX) > 6:
    g = HEX[6]
    if g == "A":
        g = 10
    elif g == "B":
        g = 11
    elif g == "C":
        g = 12
    elif g == "D":
        g = 13
    elif g == "E":
        g = 14
    elif g == "F":
        g = 15
if len(HEX) > 7:
    h = HEX[7]
    if h == "A":
        h = 10
    elif h == "B":
        h = 11
    elif h == "C":
        h = 12
    elif h == "D":
        h = 13
    elif h == "E":
        h = 14
    elif h == "F":
        h = 15
if len(HEX) > 8:
    i = HEX[8]
    if i == "A":
        i = 10
    elif i == "B":
        i = 11
    elif i == "C":
        i = 12
    elif i == "D":
        i = 13
    elif i == "E":
        i = 14
    elif i == "F":
        i = 15


if len(HEX) <= 1:
    DEC = a
elif len(HEX) <= 2:
    DEC = a + b * 16
elif len(HEX) <= 3:
    DEC = a + b * 16 + c * (16**2)
elif len(HEX) <= 4:
    DEC = a + b * 16 + c * (16**2) + d * (16**3)
elif len(HEX) <= 5:
    DEC = a + b * 16 + c * (16**2) + d * (16**3) + e(16**4)
elif len(HEX) <= 5:
    DEC = a + b * 16 + c * (16**2) + d * (16**3) + e(16**4) + f(16**5)
print("Back to decimale :", DEC)

date.today()
print("the date of execution is : " + str(date.today()))
print(sys.argv[0])
