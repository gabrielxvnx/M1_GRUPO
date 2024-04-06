import csv
from datetime import datetime, timedelta

# Classe para gerenciar o banco de dados de respostas do questionário
class BancoDeDados:
    def __init__(self):
        self.dados = {
            'idade': [],
            'genero': [],
            'resposta1': [],
            'resposta2': [],
            'resposta3': [],
            'resposta4': [],
            'hora': [],
            'data': []
        }

    def adicionar_resposta(self, respostas):
        for chave, valor in zip(self.dados.keys(), respostas):
            self.dados[chave].append(valor)

    def salvar_em_csv(self, nome_arquivo):
        with open(f'{nome_arquivo}.csv', 'w', newline='', encoding='utf-8') as file:
            colunas = list(self.dados.keys())
            escritor = csv.DictWriter(file, fieldnames=colunas, delimiter=';')
            escritor.writeheader()
            for i in range(len(self.dados['idade'])):
                escritor.writerow({coluna: self.dados[coluna][i] for coluna in colunas})

# Classe para representar o questionário e coletar dados
class Questionario:
    def __init__(self):
        self.limite_idade = [str(i) for i in range(1, 101)] + ['00']
        self.generos = ['M', 'F', 'O']
        self.tipo_resposta = ['1', '2', '3']

    def obter_resposta(self, mensagem, opcoes):
        resposta = input(mensagem).upper()
        while resposta not in opcoes:
            print('Resposta inválida, tente de novo')
            resposta = input(mensagem).upper()
        return resposta

    def transformar_resp(self, r):
        return {'1': 'Sim', '2': 'Não', '3': 'não sabe'}.get(r, r)

    def coletar_dados(self):
        # Coleta a idade
        idade = self.obter_resposta('Quantos anos você tem? (Digite um número de 1 a 100): ', self.limite_idade)
        if idade == '00':
            return False

        # Coleta o gênero e aplica o método upper()
        genero = self.obter_resposta('Qual seu gênero? (Responda com M, F ou O): ', self.generos).upper()

        # Coleta as demais respostas
        resposta1 = self.obter_resposta('Você considera sua alimentação saudável?: ', self.tipo_resposta)
        resposta2 = self.obter_resposta('Você pratica atividade física regularmente?: ', self.tipo_resposta)
        resposta3 = self.obter_resposta('Você realizou algum exame de saúde preventivo no último ano?: ', self.tipo_resposta)
        resposta4 = self.obter_resposta('Você fuma?: ', self.tipo_resposta)
        
        # Coleta a data e hora atuais ajustadas para o fuso horário desejado
        data_completa = datetime.now() - timedelta(hours=3)
        hora = data_completa.strftime('%H:%M:%S')
        data = data_completa.strftime('%d/%m/%Y')
        
        # Compila todas as respostas
        respostas = [idade, genero, resposta1, resposta2, resposta3, resposta4, hora, data]
        return [self.transformar_resp(resp) for resp in respostas]