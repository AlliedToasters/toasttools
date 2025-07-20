# components.py
import streamlit as st

def contribute_section():

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Source Code"):
            st.markdown("[github](https://github.com/AlliedToasters/toasttools)")
    

def social_badges():
    st.markdown("""
    [![GitHub stars](https://img.shields.io/github/stars/alliedtoasters/toasttools?style=social)](https://github.com/alliedtoasters/toasttools)
    [![GitHub followers](https://img.shields.io/github/followers/alliedtoasters?style=social)](https://github.com/alliedtoasters)
    [![Twitter Follow](https://img.shields.io/twitter/follow/AlliedToasters?style=social)](https://x.com/AlliedToasters)
""")
    
def boilerplate():
    social_badges()
    contribute_section()