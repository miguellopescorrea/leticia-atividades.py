km=float(input(""))
m=float(input(""))
L=float(input(""))
def conversor_km(km):
    return km/0.6
def conversor_m(m):
    return m*1000
def conversor_l(L):
    return L*1000

converter = input("")

if converter == "km":
    print("seu resultado em milhas é: ", conversor_km(km) )

elif converter == "m":
    print("seu resultado em cemtimetros ém", conversor_m(m))
elif converter == "l":
    print("seu resultado em mililitros é", conversor_l(L))
