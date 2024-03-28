import csv
from datetime import datetime , timedelta
data_completa = datetime.now()
data_completa_brasil = data_completa - timedelta(hours=3)

hora = data_completa_brasil.strftime('%H:%M:%S')
data = data_completa_brasil.strftime('%d/%m/%Y')
print(hora)
print(data)

db = {
  'idade':[],
  'genero':[],
  'resposta1':[],
  'resposta2':[],
  'resposta3':[],
  'resposta4':[]
}
opcoes_idade = [str(i) for i in range(1, 101)] 
def obter_resposta(mensagem, opcoes):
  resposta = input(mensagem)
  while resposta not in opcoes:
      resposta = input(mensagem)
  return resposta

idade = obter_resposta('Quantos anos você tem? (Digite um número de 1 a 100) ', opcoes_idade)
idade = int(idade)
genero = obter_resposta('Qual seu gênero? (Responda com M, F ou O) ', ['m', 'f', 'o','M','F','O'])

resposta1 = obter_resposta('Você considera sua alimentação saudável?', ['1', '2', '3'])
resposta2 = obter_resposta('Você pratica atividade física regularmente?', ['1', '2', '3'])
resposta3 = obter_resposta('Você realizou algum exame de saúde preventivo no último ano?', ['1', '2', '3'])
resposta4 = obter_resposta('Você fuma?', ['1', '2', '3'])


respostas = resposta1, resposta2, resposta3, resposta4

print(respostas)