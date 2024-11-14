import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2002)')

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
#retirar o unnamed
df.drop(columns=['Unnamed: 0'],inplace= True) 


#converter lat e long para numeros
list = ['Lat_d', 'Long_d']
df[list] = df[list].apply(pd.to_numeric, errors='coerce') 

estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)

dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")

qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

st.bar_chart(df['NM_UF'].value_counts())

st.bar_chart(df['NM_MUNIC'].value_counts())

st.bar_chart(df['NM_MUNIC'].value_counts()[0:10])



st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())



st.header('Os primeiros dez municípios com comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])



numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))



st.metric('# Quantidade de Municípios', len(df['NM_MUNIC'].unique()))
st.metric('# Comunidades', len(df['NM_AGLOM'].unique()))

qtdeMunicipios = len(dadosFiltrados)
st.write("A quantidade de municípios com localização quilombola do Estado selecionado é " + str(qtdeMunicipios))




