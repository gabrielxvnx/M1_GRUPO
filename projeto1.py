import streamlit as st
import pandas as pd
from datetime import datetime , timedelta



# Função para obter o estado da sessão
def get_state():
    if 'data' not in st.session_state:
        st.session_state['data'] = []
    return st.session_state['data']

# Função para adicionar um novo registro ao estado da sessão
def add_to_state(nome, idade,genero,alimentacao,atv_fisica,exame,fuma,hora,data):
    st.session_state['data'].append({'nome': nome,
                                     'idade': idade,
                                     'Gênero':genero,
                                     'alimentação saudável?':alimentacao,
                                     'atividade física regularmente?':atv_fisica,
                                     'exame de saúde no último ano?':exame,
                                     'fuma?':fuma,
                                     'hora':hora,
                                     'data':data
                                     })

# Função para converter os dados do dicionário em bytes de CSV
def convert_to_csv(data):
    dataframe = pd.DataFrame(data)
    csv_data = dataframe.to_csv(sep=';', index=False).encode('utf-8-sig')
    return csv_data

st.title('Cadastro de dados')
# Formulário para inserir novos dados
with st.form(key='my_form', clear_on_submit=True):
    nome = st.text_input(label='Nome')
    idade = st.text_input(label='Idade')
    genero = st.selectbox('Qual seu gênero?', ['Masculino','Feminino','Outro'])
    alimentacao = st.selectbox('Você considera sua alimentação saudável?', ['Sim','Não','Talvez'])
    atv_fisica= st.selectbox('Você pratica atividade física regularmente?', ['Sim','Não','Talvez'])
    exame = st.selectbox('Você realizou algum exame de saúde preventivo no último ano?', ['Sim','Não','Talvez'])
    fuma = st.selectbox('Você fuma?', ['Sim','Não','Talvez'])

    submit_button = st.form_submit_button(label='Enviar')

print()
# Quando o formulário é enviado, adicione os dados ao estado da sessão
if submit_button:
    data_completa = datetime.now()
    # data_completa_brasil = data_completa - timedelta(hours=3)
    data_completa_brasil = data_completa 
    hora = data_completa_brasil.strftime('%H:%M:%S')
    data = data_completa_brasil.strftime('%d/%m/%Y')
    add_to_state(nome, idade,genero,alimentacao,atv_fisica,exame,fuma,hora,data )
    

# Botão para baixar os dados em CSV
if st.button('Exportar dados para CSV'):
    csv = convert_to_csv(get_state())
    st.download_button(
        label="Baixar CSV",
        data=csv,
        file_name='dados.csv',
        mime='text/csv',
    )

# Mostrar os dados armazenados
st.write('Dados inseridos:')
st.write(get_state())

