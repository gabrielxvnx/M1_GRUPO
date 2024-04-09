import streamlit as st
from banco_de_dados import BancoDeDados
from questionario import Questionario
from datetime import datetime

# Instancia o banco de dados e o questionário
banco = BancoDeDados()
questionario = Questionario()

def on_continue_clicked():
    idade = st.session_state['idade']
    genero = st.session_state['genero']
    if not idade or genero not in questionario.respostasvalidas['generos']:
        st.error('Por favor, preencha sua idade e gênero antes de continuar.')
    else:
        # Avança para a próxima parte do formulário
        st.session_state['introducao_completa'] = True

def introducao_formulario():
    st.title('Bem-vindo ao Questionário de Saúde')

    # Campo para coletar a idade
    idade = st.text_input(questionario.perguntas['idade'])
    st.session_state['idade'] = idade
    
    # Verifica se a idade está no intervalo permitido ou é '00'
    if idade and (idade not in questionario.respostasvalidas['limite_idade']):
        st.error('Idade inválida. Por favor, insira um valor entre 1 e 100 ou 00 para sair.')
        return False
    elif idade == '00':
        # Aqui você pode definir o que acontece quando '00' é inserido
        st.stop()

    genero = st.radio(questionario.perguntas['genero'], questionario.respostasvalidas['generos'])
    st.session_state['genero'] = genero

    # Botão de continuação com função de callback
    st.button('Continuar', on_click=on_continue_clicked)

def on_submit_clicked():
    resposta1 = st.session_state['resposta1']
    resposta2 = st.session_state['resposta2']
    resposta3 = st.session_state['resposta3']
    resposta4 = st.session_state['resposta4']
    # Coleta a data e hora atuais
    data_completa = datetime.now()
    hora = data_completa.strftime('%H:%M:%S')
    data = data_completa.strftime('%d/%m/%Y')

    # Compila todas as respostas
    respostas = [st.session_state['idade'], st.session_state['genero'], resposta1, resposta2, resposta3, resposta4, hora, data]
    
    # Adiciona as respostas ao banco de dados e salva em CSV
    banco.adicionar_resposta(respostas)
    banco.salvar_em_csv('respostas_questionario')
    
    # Exibe a mensagem de sucesso e reinicia o estado da sessão
    st.success('Respostas registradas com sucesso!')
    st.session_state['introducao_completa'] = False

def perguntas_formulario():
    st.title('Perguntas do Questionário')

    # Campos do formulário de perguntas
    st.session_state['resposta1'] = st.radio(questionario.perguntas['resposta1'], ('Sim', 'Não', 'Não sei responder'))
    st.session_state['resposta2'] = st.radio(questionario.perguntas['resposta2'], ('Sim', 'Não', 'Não sei responder'))
    st.session_state['resposta3'] = st.radio(questionario.perguntas['resposta3'], ('Sim', 'Não', 'Não sei responder'))
    st.session_state['resposta4'] = st.radio(questionario.perguntas['resposta4'], ('Sim', 'Não', 'Não sei responder'))

    # Botão de envio com função de callback
    st.button('Enviar', on_click=on_submit_clicked)

# Verifica se a introdução foi completada para mostrar as perguntas
if 'introducao_completa' not in st.session_state or not st.session_state['introducao_completa']:
    introducao_formulario()
else:
    perguntas_formulario()
