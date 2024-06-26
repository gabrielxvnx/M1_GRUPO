import streamlit as st
from datetime import datetime
from questionario import DadosSessao

dados_sessao = DadosSessao()

st.title('Cadastro de dados')
padrao_respostas = ['Sim', 'Não', 'Não sei responder']
genero = st.radio("Selecione seu gênero:", ['Masculino', 'Feminino', 'Outro'])

with st.form(key='meu_formulario', clear_on_submit=True):
    nome = st.text_input(label='Nome')
    idade = st.number_input(label='Idade', min_value=1, max_value=100)
    dormir = st.selectbox('Você dorme entre 6 e 8 horas por dia?', padrao_respostas)
    atv_fisica = st.selectbox('Você faz atividades fisicas regulamente?', padrao_respostas)
    agua = st.selectbox('você consome pelo 3 litros de água diariamente?', padrao_respostas)
    fuma = st.selectbox('Você fuma?', padrao_respostas)
    pergunta_personalizada_1 = ""
    pergunta_personalizada_2 = ""

    if genero == 'Masculino':
        pergunta_personalizada_1 = st.selectbox('Como homem, você já evitou certos tipos de atividade física por acreditar que não são "apropriados" para o seu gênero?', padrao_respostas)
    elif genero == 'Feminino':
        pergunta_personalizada_2 = st.selectbox('Como mulher, você sente que sua escolha de atividades físicas é influenciada por preocupações com segurança?', padrao_respostas)

    submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        data_completa = datetime.now()
        data_completa_brasil = data_completa 
        hora = data_completa_brasil.strftime('%H:%M:%S')
        data = data_completa_brasil.strftime('%d/%m/%Y')
        dados_sessao.adicionar_ao_csv(nome, idade, genero, dormir, atv_fisica, agua, fuma, pergunta_personalizada_1, pergunta_personalizada_2, hora, data)

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