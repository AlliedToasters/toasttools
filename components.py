# components.py
import streamlit as st

def contribute_section():
    st.markdown("---")
    st.markdown("### 🤝 support toast")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("⭐ Star on GitHub"):
            st.markdown("[GitHub Repository](https://github.com/AlliedToasters/toasttools)")
    
    with col2:
        if st.button("🐦 Follow on Twitter"):
            st.markdown("[Twitter Profile](https://x.com/AlliedToasters)")

def social_badges():
    st.markdown("""
    [![GitHub stars](https://img.shields.io/github/stars/alliedtoasters/toasttools?style=social)](https://github.com/alliedtoasters/toasttools)
    [![GitHub followers](https://img.shields.io/github/followers/alliedtoasters?style=social)](https://github.com/alliedtoasters)
    [![Twitter Follow](https://img.shields.io/twitter/follow/AlliedToasters?style=social)](https://x.com/AlliedToasters)
""")