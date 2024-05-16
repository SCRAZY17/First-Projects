"""
HELLO WORLD
"""

N = int(input("N ="))

S = 0
P = S

for I in range(1, N + 1):
    if I % 2 == 0:
        S += 1
    else:
        P += 1
print(f"S= {S}, P= {P}")

N1 = int(input("N ="))

S1 = 0
P1 = S1

I1 = 1
while I1 < N + 1:

    if I1 % 2 == 0:
        S1 += 1
    else:
        P1 += 1
    I1 += 1
print(f"S= {S1}, P= {P1}")
