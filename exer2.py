
# #def exercicio_2(frase):
#   #cont=0
#   #for i in frase:
#     #if i == " ":
#       #cont+=1
      
#   #return cont


# #frase = input("Escreva uma frase: ")
# #print(exercicio_2(frase))


# def exercicio_2_1(frase):
  
#   cont=0
#   cont = frase.count("!")
#   #testar com for if
  
#   return cont
  
# frase = input("Escreva uma frase: ")
# print(exercicio_2_1(frase))

#fazer com o resto dos caractesres 


def exercicio_2(frase):
  
  cont=0
  letra_up = 0
  letra_low = 0
  for d in frase:
    if d.isupper():
      letra_up += 1
    else:
      letra_low += 1
      
  return letra_low,letra_up


frase = input("Escreva uma frase: ")
print(exercicio_2(frase))


