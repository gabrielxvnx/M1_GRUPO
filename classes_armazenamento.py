import streamlit as st
import pandas as pd
from datetime import datetime

class DadosSessao:
    def __init__(self):
        if 'data' not in st.session_state:
            st.session_state['data'] = []

    def obter_estado(self):
        return st.session_state['data']

    def adicionar_ao_csv(self, nome, idade, genero, alimentacao, atv_fisica, exame, fuma, pergunta_personalizada_1, pergunta_personalizada_2, hora, data):
        st.session_state['data'].append({'nome': nome,
                                         'idade': idade,
                                         'Gênero': genero,
                                         'alimentação saudável?': alimentacao,
                                         'atividade física regularmente?': atv_fisica,
                                         'exame de saúde no último ano?': exame,
                                         'fuma?': fuma,
                                         'pergunta personalizada 1': pergunta_personalizada_1,
                                         'pergunta personalizada 2': pergunta_personalizada_2,
                                         'hora': hora,
                                         'data': data
                                         })

    def converter_para_csv(self, data):
        dataframe = pd.DataFrame(data)
        csv_data = dataframe.to_csv(sep=';', index=False).encode('utf-8-sig')
        return csv_data
