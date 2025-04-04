n1 = int(input("digite o primeiro numero"))
n2 = int(input("digite o segundo numero"))
operacao= input()

def soma(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1//n2

if operacao == "soma":
  print(soma(n1,n2))

elif operacao == "subtracao":
  print(subtracao(n1,n2))

elif operacao == "multiplicacao":
  print(multiplicacao(n1,n2))
  
else:
    print(divisao(n1,n2))