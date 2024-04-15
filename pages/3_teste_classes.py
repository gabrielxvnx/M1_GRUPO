import streamlit as st
from datetime import datetime
from classes_armazenamento import DadosSessao

dados_sessao = DadosSessao()

st.title('Cadastro de dados')

genero = st.radio("Selecione seu gênero:", ['Masculino', 'Feminino', 'Outro'])

with st.form(key='meu_formulario', clear_on_submit=True):
    nome = st.text_input(label='Nome')
    idade = st.text_input(label='Idade')
    alimentacao = st.selectbox('Você considera sua alimentação saudável?', ['Sim', 'Não', 'Talvez'])
    atv_fisica = st.selectbox('Você pratica atividade física regularmente?', ['Sim', 'Não', 'Talvez'])
    exame = st.selectbox('Você realizou algum exame de saúde preventivo no último ano?', ['Sim', 'Não', 'Talvez'])
    fuma = st.selectbox('Você fuma?', ['Sim', 'Não', 'Talvez'])

    pergunta_personalizada_1 = ""
    pergunta_personalizada_2 = ""

    if genero == 'Masculino':
        pergunta_personalizada_1 = st.text_input(label='Pergunta personalizada para homens')
        pergunta_personalizada_2 = st.text_input(label='Outra pergunta personalizada para homens')
    elif genero == 'Feminino':
        pergunta_personalizada_1 = st.text_input(label='Pergunta personalizada para mulheres')
        pergunta_personalizada_2 = st.text_input(label='Outra pergunta personalizada para mulheres')
    else:
        pergunta_personalizada_1 = st.text_input(label='Pergunta personalizada para outros gêneros')
        pergunta_personalizada_2 = st.text_input(label='Outra pergunta personalizada para outros gêneros')

    submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        data_completa = datetime.now()
        data_completa_brasil = data_completa 
        hora = data_completa_brasil.strftime('%H:%M:%S')
        data = data_completa_brasil.strftime('%d/%m/%Y')
        dados_sessao.adicionar_ao_csv(nome, idade, genero, alimentacao, atv_fisica, exame, fuma, pergunta_personalizada_1, pergunta_personalizada_2, hora, data)

if st.button('Exportar dados para CSV'):
    csv = dados_sessao.converter_para_csv(dados_sessao.obter_estado())
    st.download_button(
        label="Baixar CSV",
        data=csv,
        file_name='dados.csv',
        mime='text/csv',
    )

st.write('Dados inseridos:')
st.write(dados_sessao.obter_estado())
