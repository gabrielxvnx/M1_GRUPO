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

class Questionario:
    def __init__(self):
        self.limite_idade = [str(i) for i in range(1, 101)] +['00']
        self.generos = ['m', 'f', 'o','M','F','O']
        self.tipo_resposta = ['1', '2', '3']

    def obter_resposta(self, mensagem, opcoes):
        resposta = input(mensagem)
        while resposta not in opcoes:
            print('''
            resposta invalida, tente de novo
            ''')
            resposta = input(mensagem)
        return resposta
    @staticmethod
    def transformar_resp(r):
        if r == '1':
            return 'Sim'
        elif r == '2':
            return 'Não'
        elif r == '3':
            return 'não sabe'
        else:
            return r

    def coletar_dados(self):
        idade = self.obter_resposta('Quantos anos você tem? (Digite um número de 1 a 100): ', self.limite_idade)
        if idade == '00':
            return False
        idade = int(idade)
        genero = self.obter_resposta('Qual seu gênero? (Responda com M, F ou O): ', self.generos)
        resposta1 = self.obter_resposta('Você considera sua alimentação saudável?: ', self.tipo_resposta)
        resposta2 = self.obter_resposta('Você pratica atividade física regularmente?: ', self.tipo_resposta)
        resposta3 = self.obter_resposta('Você realizou algum exame de saúde preventivo no último ano?: ', self.tipo_resposta)
        resposta4 = self.obter_resposta('Você fuma?: ', self.tipo_resposta)
        data_completa = datetime.now()
        data_completa_brasil = data_completa - timedelta(hours=3)
        hora = data_completa_brasil.strftime('%H:%M:%S')
        data = data_completa_brasil.strftime('%d/%m/%Y')
        respostas = [idade,genero,resposta1, resposta2, resposta3, resposta4,hora,data]
        respostas = list(map(self.transformar_resp, respostas))
        return respostas

def escrever_no_csv(db,nome_arquivo):
    # Abre o arquivo CSV para escrita
    with open(f'{nome_arquivo}.csv','w', newline='', encoding='utf-8') as file:
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

def main():    
    respostas = True
    print('''bem vindo ao questionario
responda: (1) para sim, (2) para não,(3) para não sei responder
    ''')
    j = False
    while respostas:
        if j:
            print('responda: (1) para sim, (2) para não,(3) para não sei responder')
        j = True
        respostas = []
        pessoa = Questionario()
        respostas = pessoa.coletar_dados()
        if respostas == False:
            break
        i = 0
        for chave, valor in db.items():
            db[chave].append(respostas[i])
            i+=1
        print('Respostas Registradas!')
    escrever_no_csv(db,'teste2')

    

main()