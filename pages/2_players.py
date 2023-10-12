import streamlit as st

st.set_page_config(page_title='Players', page_icon='🏃', layout='wide')

df = st.session_state['data']
teams = df['Club'].value_counts().index
team_select = st.sidebar.selectbox('Teams', teams)
df_players = df[df['Club'] == team_select]
players = df_players['Name'].value_counts().index
player_select = st.sidebar.selectbox('Players', players)
player_stats = df[df['Name'] == player_select].iloc[0]
st.image(player_stats['Photo'])
st.title(player_stats['Name'])
st.markdown(f"**Team:** {player_stats['Club']}")
st.markdown(f"**Position:** {player_stats['Position']}")
col_1, col_2, col_3 = st.columns(3)
col_1.markdown(f"**Age:** {player_stats['Age']}")
col_2.markdown(f"**Height:** {player_stats['Height(cm.)'] / 100}")
col_3.markdown(f"**Weight:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")
st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))
col_1, col_2, col_3 = st.columns(3)
col_1.metric(label='Value', value=f"£ {player_stats['Value(£)']:,}")
col_2.metric(label='Wage', value=f"£ {player_stats['Wage(£)']:,}")
col_3.metric(label='Release Clause',
             value=f"£ {player_stats['Release Clause(£)']:,}")
