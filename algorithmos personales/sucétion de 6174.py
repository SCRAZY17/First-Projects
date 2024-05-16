def kaprekar(numy):

    # Ensure the input number has exactly 4 digits
    num_str = str(numy).zfill(4)
    asc_num = int("".join(sorted(num_str)))
    desc_num = int("".join(sorted(num_str, reverse=True)))
    return desc_num - asc_num


numy = int(input("Enter a 4-digit number: "))
num = numy
iterations = 0
while numy != 6174 and iterations <= 8:
    numy = kaprekar(numy)
    iterations += 1

if numy == 6174:
    print("Reached the Kaprekar constant 6174 in", iterations, "iterations.")
else:
    print("Did not reach the Kaprekar constant 6174 after", iterations, "iterations.")


# my implementation:
h = 0


num = str(num)
num = num.replace("", " ")
num = num.split()

A = int(num[0])
B = int(num[1])
C = int(num[2])
D = int(num[3])

# while num < 7164 or num > 7164:
if A >= B >= C >= D:
    Z = A, B, C, D

    Y = D, C, B, A

elif A >= B >= D >= C:
    Z = A, B, D, C

    Y = C, D, B, A

elif A >= B >= C >= D:
    Z = A, B, C, D

    Y = D, C, B, A

elif A >= C >= B >= D:
    Z = A, C, B, D

    Y = D, B, C, A

elif A >= B >= C >= D:
    Z = A, B, C, D

    Y = D, C, B, A

elif A >= C >= D >= B:
    Z = A, C, D, B

    Y = B, D, C, A

elif A >= D >= C >= B:
    Z = A, D, C, B

    Y = B, C, D, A

elif A >= D >= B >= C:
    Z = A, D, B, C

    Y = C, B, D, A

elif B >= A >= C >= D:
    Z = B, A, C, D

    Y = D, C, A, B

elif B >= A >= D >= C:
    Z = B, A, D, C

    Y = C, D, A, B

elif B >= C >= A >= D:
    Z = B, C, A, D

    Y = D, A, C, B

elif B >= C >= D >= A:
    Z = B, C, D, A

    Y = A, D, C, B

elif B >= D >= A >= C:
    Z = B, D, A, C

    Y = C, A, D, B

elif B >= D >= C >= A:
    Z = B, D, C, A

    Y = A, C, D, B

elif C >= A >= B >= D:
    Z = C, A, B, D

    Y = D, B, A, C

elif C >= A >= D >= B:
    Z = C, A, D, B

    Y = B, D, A, C

elif C >= B >= D >= A:
    Z = C, B, D, A

    Y = A, D, B, C

elif C >= B >= A >= D:
    Z = C, B, A, D

    Y = D, A, B, C

elif C >= D >= A >= B:
    Z = C, D, A, B

    Y = B, A, D, C

elif C >= D >= B >= A:
    Z = C, D, B, A

    Y = A, B, D, C

elif D >= A >= B >= C:
    Z = D, A, B, C

    Y = C, B, A, D

elif D >= A >= C >= B:
    Z = D, A, C, B

    Y = B, C, A, D

elif D >= B >= C >= A:
    Z = D, B, C, A

    Y = A, C, B, D

elif D >= B >= A >= C:
    Z = D, B, A, C

    Y = C, A, B, D

elif D >= C >= A >= B:
    Z = D, C, A, B

    Y = B, A, C, D

elif D >= C >= B >= A:
    Z = D, C, B, A

    Y = A, B, C, D

Z = str(Z)
Z = Z.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
Y = str(Y)
Y = Y.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
num_1 = int(Z)
num_2 = int(Y)

print("num_1=", num_1, "num_2=", num_2)

num = num_1 - num_2
print("num=", num)
if num == 6174:
    h = None
else:
    num = str(num)
    num = num.replace("", " ")
    num = num.split()

    A = int(num[0])
    B = int(num[1])
    C = int(num[2])
    D = int(num[3])

    # while num < 7164 or num > 7164:
    if A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= B >= D >= C:
        Z = A, B, D, C

        Y = C, D, B, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= B >= D:
        Z = A, C, B, D

        Y = D, B, C, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= D >= B:
        Z = A, C, D, B

        Y = B, D, C, A

    elif A >= D >= C >= B:
        Z = A, D, C, B

        Y = B, C, D, A

    elif A >= D >= B >= C:
        Z = A, D, B, C

        Y = C, B, D, A

    elif B >= A >= C >= D:
        Z = B, A, C, D

        Y = D, C, A, B

    elif B >= A >= D >= C:
        Z = B, A, D, C

        Y = C, D, A, B

    elif B >= C >= A >= D:
        Z = B, C, A, D

        Y = D, A, C, B

    elif B >= C >= D >= A:
        Z = B, C, D, A

        Y = A, D, C, B

    elif B >= D >= A >= C:
        Z = B, D, A, C

        Y = C, A, D, B

    elif B >= D >= C >= A:
        Z = B, D, C, A

        Y = A, C, D, B

    elif C >= A >= B >= D:
        Z = C, A, B, D

        Y = D, B, A, C

    elif C >= A >= D >= B:
        Z = C, A, D, B

        Y = B, D, A, C

    elif C >= B >= D >= A:
        Z = C, B, D, A

        Y = A, D, B, C

    elif C >= B >= A >= D:
        Z = C, B, A, D

        Y = D, A, B, C

    elif C >= D >= A >= B:
        Z = C, D, A, B

        Y = B, A, D, C

    elif C >= D >= B >= A:
        Z = C, D, B, A

        Y = A, B, D, C

    elif D >= A >= B >= C:
        Z = D, A, B, C

        Y = C, B, A, D

    elif D >= A >= C >= B:
        Z = D, A, C, B

        Y = B, C, A, D

    elif D >= B >= C >= A:
        Z = D, B, C, A

        Y = A, C, B, D

    elif D >= B >= A >= C:
        Z = D, B, A, C

        Y = C, A, B, D

    elif D >= C >= A >= B:
        Z = D, C, A, B

        Y = B, A, C, D

    elif D >= C >= B >= A:
        Z = D, C, B, A

        Y = A, B, C, D

    Z = str(Z)
    Z = Z.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    Y = str(Y)
    Y = Y.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    num_1 = int(Z)
    num_2 = int(Y)

    print("num_1=", num_1, "num_2=", num_2)

    num = num_1 - num_2
    print("num=", num)
if num == 6174:
    h = None
else:
    num = str(num)
    num = num.replace("", " ")
    num = num.split()

    A = int(num[0])
    B = int(num[1])
    C = int(num[2])
    D = int(num[3])

    # while num < 7164 or num > 7164:
    if A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= B >= D >= C:
        Z = A, B, D, C

        Y = C, D, B, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= B >= D:
        Z = A, C, B, D

        Y = D, B, C, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= D >= B:
        Z = A, C, D, B

        Y = B, D, C, A

    elif A >= D >= C >= B:
        Z = A, D, C, B

        Y = B, C, D, A

    elif A >= D >= B >= C:
        Z = A, D, B, C

        Y = C, B, D, A

    elif B >= A >= C >= D:
        Z = B, A, C, D

        Y = D, C, A, B

    elif B >= A >= D >= C:
        Z = B, A, D, C

        Y = C, D, A, B

    elif B >= C >= A >= D:
        Z = B, C, A, D

        Y = D, A, C, B

    elif B >= C >= D >= A:
        Z = B, C, D, A

        Y = A, D, C, B

    elif B >= D >= A >= C:
        Z = B, D, A, C

        Y = C, A, D, B

    elif B >= D >= C >= A:
        Z = B, D, C, A

        Y = A, C, D, B

    elif C >= A >= B >= D:
        Z = C, A, B, D

        Y = D, B, A, C

    elif C >= A >= D >= B:
        Z = C, A, D, B

        Y = B, D, A, C

    elif C >= B >= D >= A:
        Z = C, B, D, A

        Y = A, D, B, C

    elif C >= B >= A >= D:
        Z = C, B, A, D

        Y = D, A, B, C

    elif C >= D >= A >= B:
        Z = C, D, A, B

        Y = B, A, D, C

    elif C >= D >= B >= A:
        Z = C, D, B, A

        Y = A, B, D, C

    elif D >= A >= B >= C:
        Z = D, A, B, C

        Y = C, B, A, D

    elif D >= A >= C >= B:
        Z = D, A, C, B

        Y = B, C, A, D

    elif D >= B >= C >= A:
        Z = D, B, C, A

        Y = A, C, B, D

    elif D >= B >= A >= C:
        Z = D, B, A, C

        Y = C, A, B, D

    elif D >= C >= A >= B:
        Z = D, C, A, B

        Y = B, A, C, D

    elif D >= C >= B >= A:
        Z = D, C, B, A

        Y = A, B, C, D

    Z = str(Z)
    Z = Z.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    Y = str(Y)
    Y = Y.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    num_1 = int(Z)
    num_2 = int(Y)

    print("num_1=", num_1, "num_2=", num_2)

    num = num_1 - num_2
    print("num=", num)
if num == 6174:
    h = None
else:
    num = str(num)
    num = num.replace("", " ")
    num = num.split()

    A = int(num[0])
    B = int(num[1])
    C = int(num[2])
    D = int(num[3])

    # while num < 7164 or num > 7164:
    if A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= B >= D >= C:
        Z = A, B, D, C

        Y = C, D, B, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= B >= D:
        Z = A, C, B, D

        Y = D, B, C, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= D >= B:
        Z = A, C, D, B

        Y = B, D, C, A

    elif A >= D >= C >= B:
        Z = A, D, C, B

        Y = B, C, D, A

    elif A >= D >= B >= C:
        Z = A, D, B, C

        Y = C, B, D, A

    elif B >= A >= C >= D:
        Z = B, A, C, D

        Y = D, C, A, B

    elif B >= A >= D >= C:
        Z = B, A, D, C

        Y = C, D, A, B

    elif B >= C >= A >= D:
        Z = B, C, A, D

        Y = D, A, C, B

    elif B >= C >= D >= A:
        Z = B, C, D, A

        Y = A, D, C, B

    elif B >= D >= A >= C:
        Z = B, D, A, C

        Y = C, A, D, B

    elif B >= D >= C >= A:
        Z = B, D, C, A

        Y = A, C, D, B

    elif C >= A >= B >= D:
        Z = C, A, B, D

        Y = D, B, A, C

    elif C >= A >= D >= B:
        Z = C, A, D, B

        Y = B, D, A, C

    elif C >= B >= D >= A:
        Z = C, B, D, A

        Y = A, D, B, C

    elif C >= B >= A >= D:
        Z = C, B, A, D

        Y = D, A, B, C

    elif C >= D >= A >= B:
        Z = C, D, A, B

        Y = B, A, D, C

    elif C >= D >= B >= A:
        Z = C, D, B, A

        Y = A, B, D, C

    elif D >= A >= B >= C:
        Z = D, A, B, C

        Y = C, B, A, D

    elif D >= A >= C >= B:
        Z = D, A, C, B

        Y = B, C, A, D

    elif D >= B >= C >= A:
        Z = D, B, C, A

        Y = A, C, B, D

    elif D >= B >= A >= C:
        Z = D, B, A, C

        Y = C, A, B, D

    elif D >= C >= A >= B:
        Z = D, C, A, B

        Y = B, A, C, D

    elif D >= C >= B >= A:
        Z = D, C, B, A

        Y = A, B, C, D

    Z = str(Z)
    Z = Z.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    Y = str(Y)
    Y = Y.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    num_1 = int(Z)
    num_2 = int(Y)

    print("num_1=", num_1, "num_2=", num_2)

    num = num_1 - num_2
    print("num=", num)
if num == 6174:
    h = None
else:
    num = str(num)
    num = num.replace("", " ")
    num = num.split()

    A = int(num[0])
    B = int(num[1])
    C = int(num[2])
    D = int(num[3])

    # while num < 7164 or num > 7164:
    if A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= B >= D >= C:
        Z = A, B, D, C

        Y = C, D, B, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= B >= D:
        Z = A, C, B, D

        Y = D, B, C, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= D >= B:
        Z = A, C, D, B

        Y = B, D, C, A

    elif A >= D >= C >= B:
        Z = A, D, C, B

        Y = B, C, D, A

    elif A >= D >= B >= C:
        Z = A, D, B, C

        Y = C, B, D, A

    elif B >= A >= C >= D:
        Z = B, A, C, D

        Y = D, C, A, B

    elif B >= A >= D >= C:
        Z = B, A, D, C

        Y = C, D, A, B

    elif B >= C >= A >= D:
        Z = B, C, A, D

        Y = D, A, C, B

    elif B >= C >= D >= A:
        Z = B, C, D, A

        Y = A, D, C, B

    elif B >= D >= A >= C:
        Z = B, D, A, C

        Y = C, A, D, B

    elif B >= D >= C >= A:
        Z = B, D, C, A

        Y = A, C, D, B

    elif C >= A >= B >= D:
        Z = C, A, B, D

        Y = D, B, A, C

    elif C >= A >= D >= B:
        Z = C, A, D, B

        Y = B, D, A, C

    elif C >= B >= D >= A:
        Z = C, B, D, A

        Y = A, D, B, C

    elif C >= B >= A >= D:
        Z = C, B, A, D

        Y = D, A, B, C

    elif C >= D >= A >= B:
        Z = C, D, A, B

        Y = B, A, D, C

    elif C >= D >= B >= A:
        Z = C, D, B, A

        Y = A, B, D, C

    elif D >= A >= B >= C:
        Z = D, A, B, C

        Y = C, B, A, D

    elif D >= A >= C >= B:
        Z = D, A, C, B

        Y = B, C, A, D

    elif D >= B >= C >= A:
        Z = D, B, C, A

        Y = A, C, B, D

    elif D >= B >= A >= C:
        Z = D, B, A, C

        Y = C, A, B, D

    elif D >= C >= A >= B:
        Z = D, C, A, B

        Y = B, A, C, D

    elif D >= C >= B >= A:
        Z = D, C, B, A

        Y = A, B, C, D

    Z = str(Z)
    Z = Z.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    Y = str(Y)
    Y = Y.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    num_1 = int(Z)
    num_2 = int(Y)

    print("num_1=", num_1, "num_2=", num_2)

    num = num_1 - num_2
    print("num=", num)
if num == 6174:
    h = None
else:
    num = str(num)
    num = num.replace("", " ")
    num = num.split()

    A = int(num[0])
    B = int(num[1])
    C = int(num[2])
    D = int(num[3])

    # while num < 7164 or num > 7164:
    if A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= B >= D >= C:
        Z = A, B, D, C

        Y = C, D, B, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= B >= D:
        Z = A, C, B, D

        Y = D, B, C, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= D >= B:
        Z = A, C, D, B

        Y = B, D, C, A

    elif A >= D >= C >= B:
        Z = A, D, C, B

        Y = B, C, D, A

    elif A >= D >= B >= C:
        Z = A, D, B, C

        Y = C, B, D, A

    elif B >= A >= C >= D:
        Z = B, A, C, D

        Y = D, C, A, B

    elif B >= A >= D >= C:
        Z = B, A, D, C

        Y = C, D, A, B

    elif B >= C >= A >= D:
        Z = B, C, A, D

        Y = D, A, C, B

    elif B >= C >= D >= A:
        Z = B, C, D, A

        Y = A, D, C, B

    elif B >= D >= A >= C:
        Z = B, D, A, C

        Y = C, A, D, B

    elif B >= D >= C >= A:
        Z = B, D, C, A

        Y = A, C, D, B

    elif C >= A >= B >= D:
        Z = C, A, B, D

        Y = D, B, A, C

    elif C >= A >= D >= B:
        Z = C, A, D, B

        Y = B, D, A, C

    elif C >= B >= D >= A:
        Z = C, B, D, A

        Y = A, D, B, C

    elif C >= B >= A >= D:
        Z = C, B, A, D

        Y = D, A, B, C

    elif C >= D >= A >= B:
        Z = C, D, A, B

        Y = B, A, D, C

    elif C >= D >= B >= A:
        Z = C, D, B, A

        Y = A, B, D, C

    elif D >= A >= B >= C:
        Z = D, A, B, C

        Y = C, B, A, D

    elif D >= A >= C >= B:
        Z = D, A, C, B

        Y = B, C, A, D

    elif D >= B >= C >= A:
        Z = D, B, C, A

        Y = A, C, B, D

    elif D >= B >= A >= C:
        Z = D, B, A, C

        Y = C, A, B, D

    elif D >= C >= A >= B:
        Z = D, C, A, B

        Y = B, A, C, D

    elif D >= C >= B >= A:
        Z = D, C, B, A

        Y = A, B, C, D

    Z = str(Z)
    Z = Z.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    Y = str(Y)
    Y = Y.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
    num_1 = int(Z)
    num_2 = int(Y)

    print("num_1=", num_1, "num_2=", num_2)

    num = num_1 - num_2
    print("num=", num)
if num == 6174:
    h = None
else:
    num = str(num)
    num = num.replace("", " ")
    num = num.split()

    A = int(num[0])
    B = int(num[1])
    C = int(num[2])
    D = int(num[3])

    # while num < 7164 or num > 7164:
    if A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= B >= D >= C:
        Z = A, B, D, C

        Y = C, D, B, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= B >= D:
        Z = A, C, B, D

        Y = D, B, C, A

    elif A >= B >= C >= D:
        Z = A, B, C, D

        Y = D, C, B, A

    elif A >= C >= D >= B:
        Z = A, C, D, B

        Y = B, D, C, A

    elif A >= D >= C >= B:
        Z = A, D, C, B

        Y = B, C, D, A

    elif A >= D >= B >= C:
        Z = A, D, B, C

        Y = C, B, D, A

    elif B >= A >= C >= D:
        Z = B, A, C, D

        Y = D, C, A, B

    elif B >= A >= D >= C:
        Z = B, A, D, C

        Y = C, D, A, B

    elif B >= C >= A >= D:
        Z = B, C, A, D

        Y = D, A, C, B

    elif B >= C >= D >= A:
        Z = B, C, D, A

        Y = A, D, C, B

    elif B >= D >= A >= C:
        Z = B, D, A, C

        Y = C, A, D, B

    elif B >= D >= C >= A:
        Z = B, D, C, A

        Y = A, C, D, B

    elif C >= A >= B >= D:
        Z = C, A, B, D

        Y = D, B, A, C

    elif C >= A >= D >= B:
        Z = C, A, D, B

        Y = B, D, A, C

    elif C >= B >= D >= A:
        Z = C, B, D, A

        Y = A, D, B, C

    elif C >= B >= A >= D:
        Z = C, B, A, D

        Y = D, A, B, C

    elif C >= D >= A >= B:
        Z = C, D, A, B

        Y = B, A, D, C

    elif C >= D >= B >= A:
        Z = C, D, B, A

        Y = A, B, D, C

    elif D >= A >= B >= C:
        Z = D, A, B, C

        Y = C, B, A, D

    elif D >= A >= C >= B:
        Z = D, A, C, B

        Y = B, C, A, D

    elif D >= B >= C >= A:
        Z = D, B, C, A

        Y = A, C, B, D

    elif D >= B >= A >= C:
        Z = D, B, A, C

        Y = C, A, B, D

    elif D >= C >= A >= B:
        Z = D, C, A, B

        Y = B, A, C, D

    elif D >= C >= B >= A:
        Z = D, C, B, A

        Y = A, B, C, D

Z = str(Z)
Z = Z.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
Y = str(Y)
Y = Y.replace("(", "").replace(",", "").replace(" ", "").replace(")", "")
num_1 = int(Z)
num_2 = int(Y)

print("num_1=", num_1, "num_2=", num_2)

num = num_1 - num_2
print("num=", num)
