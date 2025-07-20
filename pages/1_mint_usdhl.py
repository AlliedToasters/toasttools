import streamlit as st
from components import social_badges
from wallet_connect import wallet_connect

st.set_page_config(
    page_title="Mint USDHL",
    page_icon="💵",
)

st.write("# Mint USDHL Tokens 💵")
st.sidebar.success("Select a tool.")

st.markdown(
    """
    This page allows you to mint USDHL tokens on the hyperEVM network.
    Connect your wallet and enter the amount you wish to mint below.
    """
)

# Wallet connection
wallet_connection = wallet_connect(label="wallet", key="mint_wallet")

if not wallet_connection:
    st.warning("⚠️ Please connect your wallet to mint USDHL tokens")
    st.sidebar.error("🔴 Wallet Not Connected")
else:
    # Handle both string and dict responses
    if isinstance(wallet_connection, dict) and 'account' in wallet_connection:
        account = wallet_connection['account']
    elif isinstance(wallet_connection, str):
        account = wallet_connection
    else:
        account = "Connected"
    
    if len(account) > 10:
        st.success(f"✅ Wallet connected: {account[:10]}...{account[-6:]}")
        st.sidebar.success(f"🟢 Wallet Connected")
        st.sidebar.text(f"Address: {account[:6]}...{account[-4:]}")
        
        # Contract information
        st.markdown("### 📋 Contract Information")
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("**USDHL Contract Address**\n`0x...` (Coming Soon)")
        
        with col2:
            st.info("**Your Wallet**\n`" + account[:10] + "...`")
    else:
        st.success("✅ Wallet connected!")
        st.sidebar.success(f"🟢 Wallet Connected")
    
    # Minting interface
    st.markdown("### 💰 Mint Tokens")
    
    amount = st.number_input(
        "Amount to mint (in USDHL):", 
        min_value=1, 
        max_value=10000,
        step=1,
        help="Enter the number of USDHL tokens you want to mint"
    )
    
    # Estimated gas fee (placeholder)
    if amount > 0:
        estimated_gas = 0.001  # Example gas fee
        st.markdown(f"**Estimated Gas Fee:** ~{estimated_gas} ETH")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🚀 Mint USDHL Tokens", type="primary", use_container_width=True):
            if amount > 0:
                # Here you can use streamlit-wallet-connect to send the actual transaction
                # Example transaction (you'll need to replace with actual USDHL contract details):
                transaction = wallet_connect(
                    label="send",
                    key="mint_tx_unique",  # Unique key for transaction
                    message=f"Mint {amount} USDHL tokens",
                    contract_address="YOUR_USDHL_CONTRACT_ADDRESS",  # Replace with actual contract
                    amount=str(amount),
                    to_address=account if isinstance(wallet_connection, str) else wallet_connection.get('account', account)
                )
                
                if transaction:
                    st.success(f"🎉 Successfully minted {amount} USDHL tokens!")
                    st.balloons()
                    
                    # Display transaction details
                    st.markdown("### 📄 Transaction Details")
                    st.code(f"""
Transaction Hash: {transaction.get('hash', 'N/A')}
From: {wallet_connection['account'][:10]}...
To: USDHL Contract
Amount: {amount} USDHL
Status: ✅ Success
                    """)
                else:
                    st.error("Transaction failed or was cancelled")
            else:
                st.error("Please enter a valid amount to mint.")

    # Additional information
    st.markdown("---")
    st.markdown("### ℹ️ About USDHL")
    st.markdown("""
    USDHL is a stablecoin designed for the hyperEVM ecosystem. Key features:
    
    - 🔒 **Secure**: Built on proven smart contract standards
    - ⚡ **Fast**: Low-cost transactions on hyperEVM
    - 🌐 **Interoperable**: Works across multiple networks
    - 💎 **Stable**: Pegged to USD value
    """)

social_badges()