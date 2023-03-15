#programa que identifique la cara inversa en una dado "con el condicional elif"

print("----------------------------------")
print("---------CARA_INVERSA-------------")
print("----------------------------------")

#input 

c = float(input("inserte una cara del dado: "))

#processing

if 1<= c <= 6:
    if c == 1:
        print("la cara inversa de 1 es 6")
    elif c == 2:
        print("la cara inversa de 2 es 5")
    elif c== 3:
        print("la cara inversa de 3 es 4")
    elif c == 4:
        print("la cara inversa de 4 es 3")
    elif c == 5:
        print("la cara inversa de 5 es 2")
    elif c == 6:
        print("la cara inversa de 6 es 1")
    else:
        print("no es un numero entero")
else:
    print("no es la cara de un dado")