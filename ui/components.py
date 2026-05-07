import streamlit as st

def metric_card(value, title):
    st.markdown(f""" <div class="metric_card">
                          <h3> {title} </h3>
                          <h1> {value} </h3>
                     </div> """
                     ,unsafe_allow_html=True)

def alerta_critica(texto):
    st.markdown(f""" <div class="alerta_critica"> 
                        {texto}
                     </div>""", 
                     unsafe_allow_html=True)