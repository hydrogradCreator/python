from num2words import num2words

def exercicio_4(num):
    
    num_extenso =0

    if 0 <= num <= 100:
        num_extenso =  num2words(num, lang='pt-br')
    return num_extenso


numero = int(input("Digite um numero: "))
print(exercicio_4(numero))
