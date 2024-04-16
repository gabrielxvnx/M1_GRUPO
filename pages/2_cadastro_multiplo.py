import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# Senha do administrador
ADMIN_PASSWORD = "ddd"

# Caminho para o arquivo CSV
csv_file_path = 'dados.csv'

# Função para ler o CSV ou criar um novo se não existir
def read_or_create_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path, sep=';', encoding='utf-8-sig')
    else:
        # Defina as colunas do seu CSV aqui
        return pd.DataFrame(columns=['nome', 'idade', 'Gênero', 'alimentação saudável?', 'atividade física regularmente?', 'exame de saúde no último ano?', 'fuma?', 'hora', 'data'])

# Função para adicionar dados ao CSV
def add_data_to_csv(file_path, data):
    df = read_or_create_csv(file_path)
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, sep=';', index=False, encoding='utf-8-sig')
    

# Função para esvaziar o conteúdo do CSV
def clear_csv(file_path):
    empty_df = pd.DataFrame(columns=['nome', 'idade','Gênero','alimentação saudável?','atividade física regularmente?','exame de saúde no último ano?','fuma?','hora','data'])
    empty_df.to_csv(file_path, index=False)

# Crie o formulário no Streamlit
with st.form(key='my_form', clear_on_submit=True):
    nome = st.text_input(label='Nome')
    idade = st.text_input(label='Idade')
    genero = st.selectbox('Qual seu gênero?', ['Masculino','Feminino','Outro'])
    alimentacao = st.selectbox('Você considera sua alimentação saudável?', ['Sim','Não','Talvez'])
    atv_fisica= st.selectbox('Você pratica atividade física regularmente?', ['Sim','Não','Talvez'])
    exame = st.selectbox('Você realizou algum exame de saúde preventivo no último ano?', ['Sim','Não','Talvez'])
    fuma = st.selectbox('Você fuma?', ['Sim','Não','Talvez'])

    submit_button = st.form_submit_button(label='Enviar')

# Se o botão de envio for pressionado, adicione os dados ao CSV
if submit_button:
    data_completa = datetime.now()
    data_completa_brasil = data_completa - timedelta(hours=3)
    hora = data_completa_brasil.strftime('%H:%M:%S')
    data = data_completa_brasil.strftime('%d/%m/%Y')
    new_data = {'nome': nome,
                 'idade': idade,
                 'Gênero':genero,
                 'alimentação saudável?':alimentacao,
                 'atividade física regularmente?':atv_fisica,
                 'exame de saúde no último ano?':exame,
                 'fuma?':fuma,
                 'hora':hora,
                 'data':data
                 }
    add_data_to_csv(csv_file_path, new_data)
    st.success("Dados adicionados com sucesso!")

# Função para baixar o arquivo CSV
def get_csv(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

# Botão de download para o arquivo CSV
st.download_button(
    label="Baixar CSV",
    data=get_csv(csv_file_path),
    file_name='nome_do_arquivo.csv',
    mime='text/csv',
    key='download-csv'
)

# Verificação de senha para esvaziar o conteúdo do CSV
with st.expander('esvazair dados'):
    password = st.text_input("Digite a senha de administrador para esvaziar o csv:", type="password")
    if st.button('Enviar'):
        if password == ADMIN_PASSWORD:
            clear_csv(csv_file_path)
            st.success("CSV esvaziado com sucesso!")
        else:
            st.error("Senha incorreta! Apenas administradores podem esvaziar o CSV.")

