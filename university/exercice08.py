"""HELLO WORLD"""

# we've the vars= a,b,c
# if : {a**2=(b**2+c**2)**0.5 or b**2=(a**2+c**2)**0.5 or c**2=(b**2+a**2)**0.5}=true
# print ('triangle rectangle')


print("ex08:")

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

# if (
#    a == ((b**2 + c**2) ** 0.5)
#    or b == ((a**2 + c**2) ** 0.5)
#    or c == ((b**2 + a**2) ** 0.5)
# ):
#    print("triangle rectangle")
# else:
#    print("ce n'est pas un triangle réctangle")

if a == ((b**2 + c**2) ** 0.5):
    print("triangle rectangle")
elif b == ((a**2 + c**2) ** 0.5):
    print("triangle rectangle")
elif c == ((b**2 + a**2) ** 0.5):
    print("triangle rectangle")
else:
    print("ce n'est pas un triangle réctangle")
