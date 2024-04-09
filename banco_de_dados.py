import csv

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

    def salvar_em_csv(self, respostas_questionario):
        with open(f'{respostas_questionario}.csv', 'w', newline='', encoding='utf-8') as file:
            colunas = list(self.dados.keys())
            escritor = csv.DictWriter(file, fieldnames=colunas, delimiter=';')
            escritor.writeheader()
            for i in range(len(self.dados['idade'])):
                escritor.writerow({coluna: self.dados[coluna][i] for coluna in colunas})
