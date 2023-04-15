#TABUADA EM PYTHON
#Operações simples e fatorial
#exercicios de logica em python

def chamada_tabuada(tab):         #função para chamar qual a tabuada deseja
  print("Qual tabuada deseja?")
  print(tab)
  return tab

def chamada_operacao(opt):   #função para digitar o numero que quer calcular
  return opt

def opts():       #função para mostrar as operações disponiveis
  print("Qual operação deseja?")
  print("Digite :")
  print("(1) somar")
  print("(2) subtrair")
  print("(3) multiplicar")
  print("(4) Dividir")
  print("(5) Fatorial")

def opr(p):   #input para criar uma decisão das operações disponiveis
  return p

def main():  #função principal
  #chamo o objeto das funções e coloco em uma variavel
  resulttab = chamada_tabuada(tab = list(range(0,11))) 
  resultop = chamada_operacao(opt=int(input()))
  opts() #chamado as funções
  o = opr(p=int(input()))
  print("================")
    #decisões do que o usuario quer na tabuada
  if o == 1:    
    for i in resulttab:
      som = resulttab[i] + resultop  #soma
      print(f"{resultop} + {resulttab[i]} = {som}")
      
  elif o == 2:
    for i in resulttab:
      som = resulttab[i] - resultop #subtrai
      print(f"{resultop} - {resulttab[i]} = {som}")
      
  elif o == 3:
    for i in resulttab:
      som = resulttab[i] * resultop  #multiplica
      print(f"{resultop} * {resulttab[i]} = {som}")
      
  elif o == 4:
    for i in resulttab:
      som = resulttab[i] / resultop  #divide
      print(f"{resultop} / {resulttab[i]} = {som}")
  
  elif o == 5:
    print("Esta função está fora da tabuada.")
    print("Deseja calcular o fatorial de qual numero?")
    n = int(input())
    fatorial = 1
    for i in range(1, n +1):   #aqui calcula o fatoria
      fatorial *= i
    print(f"Fatorial de {n} = {fatorial}")
      
  else:
    print("Até mais !")
    

main()  #chamada da função principal





  
  
      


