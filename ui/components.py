import streamlit as st

def metric_card(label, value):
    st.markdown(f""" <div class="metric-card">
                          <h3> {label} </h3>
                          <h1> {value} </h1>
                     </div> """,
                     unsafe_allow_html=True)

def alerta_critica(texto):
    st.markdown(f""" <div class="alert-critical">
                        {texto}
                     </div>""",
                     unsafe_allow_html=True)