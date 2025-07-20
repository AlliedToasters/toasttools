import streamlit as st
from components import social_badges

# simple interface to mint USDHL tokens
st.set_page_config(
    page_title="Mint USDHL",
    page_icon="💵",
)
st.write("# Mint USDHL Tokens 💵")
st.sidebar.success("Select a tool.")
st.markdown(
    """
    This page allows you to mint USDHL tokens.
    Please enter the amount you wish to mint below.
    """
)

amount = st.number_input("Amount to mint (in USDHL):", min_value=1, step=1)

if st.button("Mint USDHL"):
    if amount > 0:
        st.success(f"Successfully minted {amount} USDHL tokens!")
    else:
        st.error("Please enter a valid amount to mint.")

social_badges()