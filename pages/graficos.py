import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from questionario import DadosSessao

# Função para carregar os dados
def carregar_dados():
    dados_sessao = DadosSessao()
    data = dados_sessao.obter_estado()
    df = pd.DataFrame(data)
    return df

# Função para plotar histograma de idades
def plotar_histograma_idades(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data=df, x='idade', bins=20, kde=True, ax=ax)
    ax.set_title('Histograma de Idades')
    ax.set_xlabel('Idade')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar contagem por gênero
def plotar_contagem_genero(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='Gênero', ax=ax)
    ax.set_title('Contagem por Gênero')
    ax.set_xlabel('Gênero')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar contagem de consumo de água
def plotar_contagem_agua(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='você consome pelo 3 litros de água diariamente?', ax=ax)
    ax.set_title('Contagem de Consumo de Água')
    ax.set_xlabel('Consumo de Água')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar contagem de hábitos de sono
def plotar_contagem_sono(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='Você dorme entre 6 e 8 horas por dia?', ax=ax)
    ax.set_title('Contagem de Hábitos de Sono')
    ax.set_xlabel('Hábitos de Sono')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar contagem de prática de atividade física
def plotar_contagem_atv_fisica(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='atividade física regularmente?', ax=ax)
    ax.set_title('Contagem de Prática de Atividade Física')
    ax.set_xlabel('Prática de Atividade Física')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar contagem de fumantes
def plotar_contagem_fumantes(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='fuma?', ax=ax)
    ax.set_title('Contagem de Fumantes')
    ax.set_xlabel('Fumante')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar contagem de respostas personalizadas (Pergunta 1)
def plotar_contagem_personalizada_1(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='pergunta personalizada 1', ax=ax)
    ax.set_title('Contagem de Respostas Personalizadas (Pergunta 1)')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar contagem de respostas personalizadas (Pergunta 2)
def plotar_contagem_personalizada_2(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='pergunta personalizada 2', ax=ax)
    ax.set_title('Contagem de Respostas Personalizadas (Pergunta 2)')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar horário de envio dos dados
def plotar_horario_envio(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    df['hora'] = pd.to_datetime(df['hora']).dt.hour
    sns.histplot(data=df, x='hora', bins=24, kde=False, ax=ax)
    ax.set_title('Horário de Envio dos Dados')
    ax.set_xlabel('Hora')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função para plotar distribuição por data de envio
def plotar_distribuicao_data_envio(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    df['data'] = pd.to_datetime(df['data'])
    df['data'].hist(ax=ax)
    ax.set_title('Distribuição por Data de Envio')
    ax.set_xlabel('Data')
    ax.set_ylabel('Contagem')
    st.pyplot(fig)

# Função principal
def main():
    st.title('Gráficos relacionados aos dados do formulário')

    df = carregar_dados()

    st.subheader('Histograma de Idades')
    plotar_histograma_idades(df)

    st.subheader('Contagem por Gênero')
    plotar_contagem_genero(df)

    st.subheader('Contagem de Consumo de Água')
    plotar_contagem_agua(df)

    st.subheader('Contagem de Hábitos de Sono')
    plotar_contagem_sono(df)

    st.subheader('Contagem de Prática de Atividade Física')
    plotar_contagem_atv_fisica(df)

    st.subheader('Contagem de Fumantes')
    plotar_contagem_fumantes(df)

    st.subheader('Contagem de Respostas Personalizadas (Pergunta 1)')
    plotar_contagem_personalizada_1(df)

    st.subheader('Contagem de Respostas Personalizadas (Pergunta 2)')
    plotar_contagem_personalizada_2(df)

    st.subheader('Horário de Envio dos Dados')
    plotar_horario_envio(df)

    st.subheader('Distribuição por Data de Envio')
    plotar_distribuicao_data_envio(df)

if __name__ == "__main__":
    main()
