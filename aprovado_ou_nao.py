n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))

def knuckles(a, b, c):
    return (a + b + c) / 3 

if knuckles(n1, n2, n3) >= 7:  
    print("Aprovado")
else:
    print("Não sei não")
