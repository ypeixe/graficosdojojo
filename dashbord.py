import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


df = pd.read_excel("commitment_detail_2023_prefeitura.xlsx")


st.title("Dashboard de Finanças Públicas - 2023")


st.subheader("Análise de Empenhos e Distribuição por Órgão")


selected_orgao = st.selectbox("Selecione um Órgão", df['órgão'].unique())


filtered_df = df[df['órgão'] == selected_orgao]


st.write(f"Visualizando dados para o Órgão: {selected_orgao}")
st.dataframe(filtered_df)


fig_bar = px.bar(filtered_df, x='função', y='empenhado', 
                 labels={'empenhado': 'Valor Empenhado'},
                 title=f'Empenhado por Função ({selected_orgao})')
st.plotly_chart(fig_bar)


fig_pie = px.pie(filtered_df, names='função', 
                 title=f'Distribuição por Função ({selected_orgao})')
st.plotly_chart(fig_pie)


fig_scatter = go.Figure()

fig_scatter.add_trace(go.Scatter(x=filtered_df['empenhado'], y=filtered_df['liquidado'],
                                mode='markers',
                                marker=dict(size=12, color='blue'),
                                text=filtered_df['função'],
                                name='Funções'))

fig_scatter.update_layout(title=f'Relação entre Empenhado e Liquidado ({selected_orgao})',
                          xaxis=dict(title='Valor Empenhado'),
                          yaxis=dict(title='Valor Liquidado'),
                          showlegend=True)

st.plotly_chart(fig_scatter)

