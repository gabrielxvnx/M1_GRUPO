# M1_GRUPO
# README - Sistema de Cadastro e Análise de Dados

Este projeto foi desenvolvido em grupo durante o Módulo 1 por Delson, Airton, Gabriel Vinicius e Marlon. Consiste em um sistema de cadastro de informações pessoais e hábitos de saúde, dividido em duas partes principais:

1. **Terminal Python (`main.py`)**
2. **Aplicação Web com Streamlit (`app.py`)**

## 1. Terminal Python (`main.py`)

### Descrição do Código
O arquivo `main.py` contém um programa Python que roda no terminal e permite cadastrar respostas a um questionário. Ele utiliza a biblioteca `csv` para armazenar os dados em um arquivo CSV.

### Funcionalidades
- Coleta de dados pessoais e respostas a um questionário sobre hábitos de saúde.
- Registro de idade, gênero, e respostas sobre alimentação saudável, atividade física, exames de saúde preventivos e hábito de fumar.
- Armazenamento das respostas em um arquivo CSV.

## 2. Aplicação Web com Streamlit (`app.py`)

### Descrição do Código
O arquivo `app.py` contém uma aplicação web desenvolvida com Streamlit. Ele permite o cadastro de dados pessoais e hábitos de saúde de forma interativa em um formulário.

### Funcionalidades
- Cadastro de nome, idade, gênero e respostas a perguntas sobre hábitos de saúde.
- Geração de gráficos com base nos dados cadastrados.
- Exportação dos dados cadastrados para um arquivo CSV.
- Visualização de gráficos com dados cadastrados anteriormente.

### Cadastro Múltiplo

Além do formulário principal na aplicação web, este projeto também oferece a funcionalidade de cadastro múltiplo de dados. Esse recurso está implementado no arquivo `pages/2_cadastro_multiplo.py`. Ele permite que várias pessoas na mesma rede cadastrem seus dados simultaneamente em um único arquivo CSV compartilhado.

### Como Funciona o Cadastro Múltiplo

1. Uma pessoa inicia a aplicação web e acessa a página de cadastro múltiplo.
2. Essa pessoa define uma senha de acesso ao sistema.
3. Outros usuários conectados à mesma rede acessam a página de cadastro múltiplo e inserem seus dados.
4. Os dados inseridos pelos usuários são adicionados ao arquivo CSV compartilhado.
5. Qualquer pessoa na rede com acesso ao programa pode baixar o arquivo CSV atualizado com todos os dados cadastrados.

### Execução do Projeto

Para executar o projeto:

1. **Terminal Python**:
   - Execute o arquivo `main.py` em um terminal Python.
   - Siga as instruções para cadastrar as respostas ao questionário.

2. **Aplicação Web com Streamlit**:
   - No terminal, execute o seguinte comando para iniciar a aplicação web: 
     ```
     python -m streamlit run app.py
     ```
   - Acesse a aplicação web no navegador conforme as instruções exibidas no terminal.

## Requisitos

- Python 3.x
- Bibliotecas: `csv`, `datetime`, `streamlit`, `pandas`, `matplotlib`, `seaborn`

## Autores

Este projeto foi desenvolvido por Delson, Airton, Gabriel Vinicius e Marlon.

---
Este README fornece uma visão detalhada do projeto, suas funcionalidades, incluindo o cadastro múltiplo, e instruções para execução. Para detalhes específicos sobre implementação, consulte os comentários nos códigos-fonte fornecidos.
