def imprimir_contagem():
  
  for numero in range(21):
    print(numero)

imprimir_contagem()



def imprimir_contagem_ate_numero_digitado():
  
  numero = int(input("Digite um número: "))
  for numero in range(numero + 1):
    print(numero)


imprimir_contagem_ate_numero_digitado()

def tabuada_de_adicao_dois():
    print("Tabuada de 2")
    
    for i in range(1, 11):
        resultado = 2 + i
        print("2 + ", i, "=", resultado)

tabuada_de_adicao_dois()

def tabuada_de_multiplicacao():
    numero = int(input("Qual Tabuada de multiplicação deseja?: "))
        
    for i in range(1, 11):
        resultado = numero * i
        print(numero, " x ", i, "=", resultado)


tabuada_de_multiplicacao()