import streamlit as st
from components import social_badges

st.set_page_config(
    page_title="toasttools",
    page_icon="",
)

st.write("# welcome to toasttools! 👋")

st.sidebar.success("select a tool.")

st.markdown(
    """
    toasttools
    **👈 select an app on the sidebar**
    of what Streamlit can do!
    ### Contribute
    - evm and hypercore address: `0x4F17562C9a6cCFE47c3ef4245eb53c047Cb2Ff1D`
"""
)

social_badges()