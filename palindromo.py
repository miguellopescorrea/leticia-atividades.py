def palindromo(palavra):
    return palavra == palavra[::-1]
def main():
    a=input("digite uma palavra")
    print(palindromo(a))    
main()
