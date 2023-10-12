import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(page_title='Home', page_icon='🏃', layout='wide')

if 'data' not in st.session_state:
    df = pd.read_csv('data/CLEAN_FIFA23_official_data.csv', index_col=0)
    df = df[df['Contract Valid Until'] >= datetime.today().year]
    df = df[df['Value(£)'] > 0]
    df = df.sort_values(by='Overall', ascending=True)
    st.session_state['data'] = df

st.write('# FIFA23 OFFICIAL DATASET! ⚽')
st.sidebar.markdown(
    'Desenvolvido por [Asinov Academy][https://link.asinov.academy.com]')

st.markdown("""
    The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. 
            
    With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.
""")

button = st.button('Acesse os dados no Kaggle')
if button:
    webbrowser.open_new_tab(
        'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')
