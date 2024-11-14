import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titolo dell'app
st.title('Esempio di Analisi Dati con Streamlit')

# Descrizione
st.write("""
    Questa è una semplice applicazione Streamlit che permette di generare un DataFrame,
    visualizzare alcune statistiche e creare un grafico.
""")

# Generazione di un DataFrame con valori casuali
st.subheader('Generazione di un DataFrame')
num_righe = st.slider('Seleziona il numero di righe', 10, 100, 30)
num_colonne = st.slider('Seleziona il numero di colonne', 2, 10, 5)

# Crea un DataFrame con valori casuali
df = pd.DataFrame(np.random.randn(num_righe, num_colonne), columns=[f'Colonna {i+1}' for i in range(num_colonne)])

# Mostra il DataFrame
st.write('DataFrame generato:', df)

# Statistiche
st.subheader('Statistiche descrittive')
st.write(df.describe())

# Grafico
st.subheader('Grafico a dispersione delle prime due colonne')
fig, ax = plt.subplots()
ax.scatter(df.iloc[:, 0], df.iloc[:, 1], c='blue', alpha=0.5)
ax.set_xlabel('Colonna 1')
ax.set_ylabel('Colonna 2')
st.pyplot(fig)

# Sezione interattiva
st.subheader('Selezione dei dati')
colonna_selezionata = st.selectbox('Seleziona una colonna per visualizzare i valori', df.columns)
st.write(f'Valori della colonna "{colonna_selezionata}":')
st.write(df[colonna_selezionata])

# Aggiungi un pulsante per aggiornare il DataFrame
if st.button('Aggiorna DataFrame'):
    df = pd.DataFrame(np.random.randn(num_righe, num_colonne), columns=[f'Colonna {i+1}' for i in range(num_colonne)])
    st.write('DataFrame aggiornato:', df)
