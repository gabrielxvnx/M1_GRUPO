from questionario import Questionario
from banco_de_dados import BancoDeDados

banco = BancoDeDados()
questionario = Questionario()

# Função principal que executa o questionário e salva as respostas
def main():
    print('Bem-vindo ao questionário')
    print('Responda: (1) para sim, (2) para não, (3) para não sei responder')
    
    while True:
        respostas = questionario.coletar_dados()
        if not respostas:
            break
        banco.adicionar_resposta(respostas)
        print('Respostas Registradas!')
    
    banco.salvar_em_csv('respostas_questionario')

if __name__ == '__main__':
    main()
