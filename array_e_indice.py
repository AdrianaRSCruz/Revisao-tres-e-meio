def imprimir_nomes():
 
    nomes = ["Adriana", "Flávia", "Rodrigo", "Pedro"]
    print("1. ", nomes[0])
    print("2. ", nomes[1])
    print("3. ", nomes[2])
    print("4. ", nomes[3])  
  

imprimir_nomes()

def imprimir_primeiro_e_ultimo_nome():
  
  nomes = ["Adriana", "Flávia", "Rodrigo", "Pedro"]
  print("Primeiro nome: ", (nomes[0]))

  print("Último nome: ", (nomes[3]))

imprimir_primeiro_e_ultimo_nome()

def imprimir_primeiro_e_ultimo_nome():
  
  nomes = ["Adriana", "Flávia", "Rodrigo", "Pedro"]
  print("Segundo nome: ", (nomes[1]))

  print("Terceiro nome: ", (nomes[2]))

imprimir_primeiro_e_ultimo_nome()


def substituir_alimentos():
  
  alimentos = ["Macarrão", "Pepino", "Batata"]
  novos_alimentos = []

  for i in range(3):

      novo_alimento = input("Digite novo alimento: " )
      novos_alimentos.append(novo_alimento)
  alimentos = novos_alimentos
  
  print("alimentos atualizados: ", alimentos)  
      
substituir_alimentos()