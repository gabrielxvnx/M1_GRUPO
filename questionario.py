from datetime import datetime, timedelta

# Classe para representar o questionário e coletar dados
class Questionario:
    def __init__(self):
        self.perguntas = {
            'idade': 'Quantos anos você tem? (Digite um número de 1 a 100): ',
            'genero': 'Qual seu gênero? (Responda com M, F ou O): ',
            'resposta1': 'Você considera sua alimentação saudável?: ',
            'resposta2': 'Você pratica atividade física regularmente?: ',
            'resposta3': 'Você realizou algum exame de saúde preventivo no último ano?: ',
            'resposta4': 'Você fuma?: ',
        }
        self.respostasvalidas = {
            'limite_idade': [str(i) for i in range(1, 101)] + ['00'],
            'generos': ['M', 'F', 'O'],
            'tipo_resposta': ['1', '2', '3'],    
        }

    def obter_resposta(self, mensagem, opcoes):
        resposta = input(mensagem).upper()
        while resposta not in opcoes:
            print('Resposta inválida, tente de novo')
            resposta = input(mensagem).upper()
        return resposta

    def transformar_resp(self, r):
        return {'1': 'Sim', '2': 'Não', '3': 'Não sei responder'}.get(r, r)

    def coletar_dados(self):
        # Coleta a idade
        idade = self.obter_resposta(self.perguntas['idade'], self.respostasvalidas['limite_idade'])
        if idade not in self.respostasvalidas['limite_idade']:
            print('Idade inválida. Por favor, insira um valor entre 1 e 100 ou 00 para sair.')
            return False

        # Coleta o gênero
        genero = self.obter_resposta(self.perguntas['genero'], self.respostasvalidas['generos'])

        # Coleta as demais respostas
        resposta1 = self.obter_resposta(self.perguntas['resposta1'], self.respostasvalidas['tipo_resposta'])
        resposta2 = self.obter_resposta(self.perguntas['resposta2'], self.respostasvalidas['tipo_resposta'])
        resposta3 = self.obter_resposta(self.perguntas['resposta3'], self.respostasvalidas['tipo_resposta'])
        resposta4 = self.obter_resposta(self.perguntas['resposta4'], self.respostasvalidas['tipo_resposta'])
        
        # Coleta a data e hora atuais ajustadas para o fuso horário desejado
        data_completa = datetime.now() - timedelta(hours=3)
        hora = data_completa.strftime('%H:%M:%S')
        data = data_completa.strftime('%d/%m/%Y')
        
        # Compila todas as respostas
        respostas = [idade, genero, resposta1, resposta2, resposta3, resposta4, hora, data]
        return [self.transformar_resp(resp) for resp in respostas]
