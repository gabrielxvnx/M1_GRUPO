import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# Senha do administrador
ADMIN_PASSWORD = "ddd"

# Caminho para o arquivo CSV
csv_file_path = 'dados.csv'
# Padrão de respotas
padrao_respostas = ['Sim', 'Não', 'Não sei responder']

# Função para ler o CSV ou criar um novo se não existir
def read_or_create_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path, sep=';', encoding='utf-8-sig')
    else:
        # Defina as colunas do seu CSV aqui
        return pd.DataFrame(columns=['nome', 'idade','Gênero','Você dorme entre 6 e 8 horas por dia?','atividade física regularmente?','você consome pelo 3 litros de água diariamente?','fuma?','pergunta personalizada 1','pergunta personalizada 2','hora','data'])

# Função para adicionar dados ao CSV
def add_data_to_csv(file_path, data):
    df = read_or_create_csv(file_path)
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, sep=';', index=False, encoding='utf-8-sig')
    

# Função para esvaziar o conteúdo do CSV
def clear_csv(file_path):
    empty_df = pd.DataFrame(columns=['nome', 'idade','Gênero','Você dorme entre 6 e 8 horas por dia?','atividade física regularmente?','você consome pelo 3 litros de água diariamente?','fuma?','pergunta personalizada 1','pergunta personalizada 2','hora','data'])
    empty_df.to_csv(file_path, sep=';', index=False)

genero = st.radio("Selecione seu gênero:", ['Masculino', 'Feminino', 'Outro'])
# Crie o formulário no Streamlit
with st.form(key='my_form', clear_on_submit=True):
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

# Se o botão de envio for pressionado, adicione os dados ao CSV
if submit_button:
    data_completa = datetime.now()
    data_completa_brasil = data_completa 
    hora = data_completa_brasil.strftime('%H:%M:%S')
    data = data_completa_brasil.strftime('%d/%m/%Y')
    new_data = {'nome': nome,
                'idade': idade,
                'Gênero': genero,
                'Você dorme entre 6 e 8 horas por dia?': dormir,
                'atividade física regularmente?': atv_fisica,
                'você consome pelo 3 litros de água diariamente?': agua,
                'fuma?': fuma,
                'pergunta personalizada 1': pergunta_personalizada_1,
                'pergunta personalizada 2': pergunta_personalizada_2,
                'hora': hora,
                'data': data
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

