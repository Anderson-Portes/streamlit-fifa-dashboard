import streamlit as st

st.set_page_config(page_title='Teams', page_icon='⚽', layout='wide')

df = st.session_state['data']
teams = df['Club'].value_counts().index
team_select = st.sidebar.selectbox('Teams', teams)
df_players = df[df['Club'] == team_select].set_index('Name')
st.image(df_players.iloc[0]['Club Logo'])
st.markdown(f"## {team_select}")

columns = ['Age', 'Photo', 'Flag', 'Overall',
           'Value(£)', 'Wage(£)', 'Joined', 'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_players[columns], column_config={
    'Overall': st.column_config.ProgressColumn('Overall', format="%d", min_value=0, max_value=100),
    'Value(£)': st.column_config.NumberColumn(),
    'Wage(£)': st.column_config.ProgressColumn('Weekly Wage', format="£%f", min_value=0, max_value=df_players['Wage(£)'].max()),
    'Photo': st.column_config.ImageColumn(),
    'Flag': st.column_config.ImageColumn('Country')
}, height=1000)
