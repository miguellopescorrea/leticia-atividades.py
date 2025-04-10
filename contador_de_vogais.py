vogais=["a","e","i","o","u"]
frase=input("")
def contador(a):
    contagem=0
    for i in a:
        if i in vogais:
            contagem+=1
    return contagem
print(contador(frase))
