import streamlit as st
import streamlit.components.v1 as components
from components import social_badges

st.set_page_config(
    page_title="toasttools",
    page_icon="🔥",
)

st.write("# welcome to toasttools! 🔥")

# Wallet connection section
st.markdown("## 🔗 Connect Your Wallet")

# Let's try a working approach using HTML/JS directly
def wallet_connect_simple():
    """Simple wallet connection using HTML/JS components"""
    
    wallet_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.10.0/web3.min.js"></script>
        <style>
            .wallet-container {
                padding: 20px;
                border-radius: 10px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
                margin: 10px 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .connect-btn {
                background: rgba(255, 255, 255, 0.2);
                border: 2px solid rgba(255, 255, 255, 0.3);
                color: white;
                padding: 15px 30px;
                border-radius: 25px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
                transition: all 0.3s ease;
                margin: 10px;
            }
            .connect-btn:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
            }
            .wallet-info {
                background: rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 8px;
                margin: 10px 0;
            }
            .status {
                font-size: 18px;
                margin-bottom: 15px;
            }
            .connected { color: #4CAF50; }
            .disconnected { color: #f44336; }
        </style>
    </head>
    <body>
        <div class="wallet-container">
            <div id="wallet-status" class="status disconnected">
                🔴 Wallet Not Connected
            </div>
            
            <div id="connect-section">
                <button class="connect-btn" onclick="connectWallet()">
                    🦊 Connect MetaMask
                </button>
            </div>
            
            <div id="wallet-info" style="display: none;">
                <div class="wallet-info">
                    <div><strong>Address:</strong> <span id="wallet-address"></span></div>
                    <div><strong>Network:</strong> <span id="network-name"></span></div>
                    <button class="connect-btn" onclick="disconnectWallet()" style="font-size: 14px; padding: 8px 16px;">
                        Disconnect
                    </button>
                </div>
            </div>
        </div>

        <script>
            let web3;
            let userAccount;

            async function connectWallet() {
                if (typeof window.ethereum !== 'undefined') {
                    try {
                        // Request account access
                        const accounts = await window.ethereum.request({
                            method: 'eth_requestAccounts'
                        });
                        
                        userAccount = accounts[0];
                        web3 = new Web3(window.ethereum);
                        
                        // Update UI
                        document.getElementById('wallet-status').innerHTML = '🟢 Wallet Connected';
                        document.getElementById('wallet-status').className = 'status connected';
                        document.getElementById('wallet-address').textContent = 
                            userAccount.substring(0, 6) + '...' + userAccount.substring(38);
                        
                        // Get network
                        const chainId = await web3.eth.getChainId();
                        const networkNames = {
                            1: 'Ethereum Mainnet',
                            137: 'Polygon',
                            56: 'BSC Mainnet'
                        };
                        document.getElementById('network-name').textContent = 
                            networkNames[chainId] || `Chain ID: ${chainId}`;
                        
                        // Show wallet info, hide connect button
                        document.getElementById('wallet-info').style.display = 'block';
                        document.getElementById('connect-section').style.display = 'none';
                        
                        // Send data to Streamlit parent
                        window.parent.postMessage({
                            type: 'streamlit:setComponentValue',
                            value: {
                                connected: true,
                                address: userAccount,
                                chainId: chainId
                            }
                        }, '*');
                        
                    } catch (error) {
                        console.error('Error connecting wallet:', error);
                        alert('Failed to connect wallet: ' + error.message);
                    }
                } else {
                    alert('MetaMask is not installed! Please install MetaMask and refresh the page.');
                    window.open('https://metamask.io/download/', '_blank');
                }
            }

            function disconnectWallet() {
                userAccount = null;
                
                // Update UI
                document.getElementById('wallet-status').innerHTML = '🔴 Wallet Not Connected';
                document.getElementById('wallet-status').className = 'status disconnected';
                document.getElementById('wallet-info').style.display = 'none';
                document.getElementById('connect-section').style.display = 'block';
                
                // Send disconnect to Streamlit parent
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: {
                        connected: false,
                        address: null,
                        chainId: null
                    }
                }, '*');
            }

            // Check for existing connection on load
            window.addEventListener('load', async () => {
                if (typeof window.ethereum !== 'undefined') {
                    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                    if (accounts.length > 0) {
                        userAccount = accounts[0];
                        connectWallet();
                    }
                }
            });
        </script>
    </body>
    </html>
    """
    
    return components.html(wallet_html, height=200)

# Use the simple wallet connector
wallet_data = wallet_connect_simple()

# Initialize session state
if 'wallet_connected' not in st.session_state:
    st.session_state.wallet_connected = False
if 'wallet_address' not in st.session_state:
    st.session_state.wallet_address = None

# Process wallet data
if wallet_data and isinstance(wallet_data, dict):
    if wallet_data.get('connected'):
        st.session_state.wallet_connected = True
        st.session_state.wallet_address = wallet_data.get('address')
        
        account = wallet_data['address']
        st.success(f"✅ Wallet connected: {account[:10]}...{account[-6:]}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Address", f"{account[:6]}...{account[-4:]}")
        with col2:
            chain_id = wallet_data.get('chainId', 'Unknown')
            st.metric("Chain ID", chain_id)
        
        st.sidebar.success("🟢 Wallet Connected")
        st.sidebar.text(f"Address: {account[:6]}...{account[-4:]}")
    else:
        st.session_state.wallet_connected = False
        st.session_state.wallet_address = None
        st.sidebar.error("🔴 Wallet Not Connected")
else:
    st.sidebar.error("🔴 Wallet Not Connected")

if not st.session_state.wallet_connected:
    st.info("👆 Click the 'Connect MetaMask' button above")

st.sidebar.success("select a tool.")

st.markdown(
    """
    ## About toasttools
    
    toasttools is a collection of Web3 utilities for hypercore and hyperEVM networks.
    
    **👈 Select an app from the sidebar** to explore what toasttools can do!
    
    ### Available Tools:
    - 💵 **Mint USDHL**: Create USDHL tokens
    - 🔄 **Multisig Send**: Multi-signature transactions (coming soon)
    
    ### 💝 Support Toast
    - EVM and Hypercore address: `0x4F17562C9a6cCFE47c3ef4245eb53c047Cb2Ff1D`
    
    ### 🛠️ Built With
    - Streamlit for the frontend
    - Custom Web3 component with MetaMask integration
    - Direct HTML/JavaScript wallet connection
"""
)

social_badges()