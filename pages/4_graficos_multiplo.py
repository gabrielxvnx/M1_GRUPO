import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
df = pd.read_csv('dados.csv', sep=';')

# Configurar o estilo dos gráficos do seaborn
sns.set(style="whitegrid")

# Ordenar os dados por idade em ordem decrescente
df_sorted = df.sort_values(by='idade', ascending=False)

# Organizar os gráficos em colunas no Streamlit
col1, col2 = st.columns(2)

# Gráfico 1: Histograma de Idades
with col1:
    st.subheader('Distribuição de Idades')
    plt.figure(figsize=(8, 6))
    sns.histplot(df_sorted['idade'], bins=20, kde=True, color='skyblue')
    plt.xlabel('Idade')
    plt.ylabel('Contagem')
    hist_fig = plt.gcf()  # Obter a figura atual
    st.pyplot(hist_fig)  # Passar a figura para st.pyplot()

# Gráfico 2: Contagem por Gênero
with col2:
    st.subheader('Contagem por Gênero')
    plt.figure(figsize=(6, 6))
    sns.countplot(data=df, x='Gênero', order=df['Gênero'].value_counts().index)
    plt.xlabel('Gênero')
    plt.ylabel('Contagem')
    gender_fig = plt.gcf()  # Obter a figura atual
    st.pyplot(gender_fig)  # Passar a figura para st.pyplot()

# Gráfico 3: Contagem de Hábitos de Sono
with col1:
    st.subheader('Você dorme entre 6 e 8 horas por dia?')
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Você dorme entre 6 e 8 horas por dia?', order=df['Você dorme entre 6 e 8 horas por dia?'].value_counts().index)
    plt.xlabel('Hábitos de Sono')
    plt.ylabel('Contagem')
    sleep_fig = plt.gcf()  # Obter a figura atual
    st.pyplot(sleep_fig)  # Passar a figura para st.pyplot()

# Gráfico 4: Contagem de Prática de Atividade Física
with col2:
    st.subheader('Pratica atividade física regularmente?')
    plt.figure(figsize=(6, 6))
    sns.countplot(data=df, x='atividade física regularmente?', order=df['atividade física regularmente?'].value_counts().index)
    plt.xlabel('Prática de Atividade Física')
    plt.ylabel('Contagem')
    physical_fig = plt.gcf()  # Obter a figura atual
    st.pyplot(physical_fig)  # Passar a figura para st.pyplot()

# Gráfico 5: Contagem de Consumo de Água
with col1:
    st.subheader('Consome pelo 3 litros de água diariamente?')
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='você consome pelo 3 litros de água diariamente?', order=df['você consome pelo 3 litros de água diariamente?'].value_counts().index)
    plt.xlabel('Consumo de Água')
    plt.ylabel('Contagem')
    water_fig = plt.gcf()  # Obter a figura atual
    st.pyplot(water_fig)  # Passar a figura para st.pyplot()

# Gráfico 6: Gráfico de Pizza para Contagem de Fumantes
with col2:
    st.subheader('Distribuição de Fumantes')
    fuma_count = df['fuma?'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(fuma_count, labels=fuma_count.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen'])
    plt.title('Distribuição de Fumantes')
    pie_fig = plt.gcf()  # Obter a figura atual
    st.pyplot(pie_fig)  # Passar a figura para st.pyplot()
