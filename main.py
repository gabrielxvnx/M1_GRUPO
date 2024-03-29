import csv
from datetime import datetime , timedelta




db = {
  'idade':[],
  'genero':[],
  'resposta1':[],
  'resposta2':[],
  'resposta3':[],
  'resposta4':[],
  'hora':[],
  'data':[]
}

def transformar_resp(r):
  if r == '1':
    return 'Sim'
  elif r == '2':
    return 'Não'
  elif r == '3':
    return 'não sabe'
  else:
    return r


opcoes_idade = [str(i) for i in range(1, 101)] 
def obter_resposta(mensagem, opcoes):
  resposta = input(mensagem)
  while resposta not in opcoes:
      resposta = input(mensagem)
  return resposta

for j in range(2):
  if j ==0:
    print('''bem vindo ao questionario
    responda: (1) para sim, (2) para não,(3) para não sei responder
    ''')
  else:
    print('''
    responda: (1) para sim, (2) para não,(3) para não sei responder
    ''')
    
  idade = obter_resposta('Quantos anos você tem? (Digite um número de 1 a 100) ', opcoes_idade)
  idade = int(idade)
  genero = obter_resposta('Qual seu gênero? (Responda com M, F ou O) ', ['m', 'f', 'o','M','F','O'])
  resposta1 = obter_resposta('Você considera sua alimentação saudável?', ['1', '2', '3'])
  resposta2 = obter_resposta('Você pratica atividade física regularmente?', ['1', '2', '3'])
  resposta3 = obter_resposta('Você realizou algum exame de saúde preventivo no último ano?', ['1', '2', '3'])
  resposta4 = obter_resposta('Você fuma?', ['1', '2', '3'])
  data_completa = datetime.now()
  data_completa_brasil = data_completa - timedelta(hours=3)
  hora = data_completa_brasil.strftime('%H:%M:%S')
  data = data_completa_brasil.strftime('%d/%m/%Y')
  print('')
  print('respostas registradas com sucesso!\n')
  respostas = [idade,genero,resposta1, resposta2, resposta3, resposta4,hora,data]
  resposta_certa = list(map(transformar_resp, respostas))
  
  i = 0
  for chave, valor in db.items():
    db[chave].append(resposta_certa[i])
    i+=1
  

print(db)

# Abre o arquivo CSV para escrita
with open('arquivo.csv','w', newline='', encoding='utf-8') as file:
    # Define os nomes das colunas0,
    colunas = ['idade', 'genero','resposta1','resposta2','resposta3','resposta4','hora','data']

    # Cria o escritor CSV usando DictWriter
    escritor = csv.DictWriter(file, fieldnames=colunas, delimiter=';')

    # Escreve o cabeçalho (nomes das colunas)
    escritor.writeheader()

    # Escreve os dados
    for i in range(len(db['idade'])):
        linha = {'idade': db['idade'][i],
                 'genero': db['genero'][i],
                 'resposta1': db['resposta2'][i],
                 'resposta2': db['resposta2'][i],
                 'resposta3': db['resposta3'][i],
                 'resposta4': db['resposta4'][i],
                 'hora': db['hora'][i],
                 'data': db['data'][i]
                }
        escritor.writerow(linha)
