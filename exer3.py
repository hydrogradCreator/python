
def exercicio_3(cpf):
  flag = True
  
  if((cpf[3] != ".") or (cpf[7]!= ".") or (cpf[-3] != "-")):
    return None
  elif(len(cpf) != 14):
    flag = False
  else:
    flag = True

  return flag
  