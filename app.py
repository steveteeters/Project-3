import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('RCSAbi.json')) as f:
        rcs_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract and is static thus needing updates if the contract adress changes
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")  
    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=rcs_abi
    )

    return contract


# Load the contract
contract = load_contract()

################################################################################
# RCS Token Contract
################################################################################
st.title("RCS Coin")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
if st.sidebar.button("Coin Information"):
    
    st.sidebar.write("Token Name:")
    st.sidebar.write(contract.caller.name())
    st.sidebar.write("Token Symbol:")
    st.sidebar.write(contract.caller.symbol())
    st.sidebar.write("Token Supply:")
    st.sidebar.write(contract.caller.totalSupply())
if st.sidebar.button("Send Money"):
    st.sidebar.write("Send Money:")
    st.sidebar.write(contract.caller.sendMoney())
if st.sidebar.button("Buy Coins"):
    st.sidebar.write("Buy:")
    st.sidebar.write(contract.caller.buy())
if st.sidebar.button("BurnCoins"):
    st.sidebar.write("Burn Coins:")
    st.sidebar.write(contract.caller.burn())
if st.sidebar.button("Contract Info"):
    st.sidebar.write("Contract Balance in:")
    st.sidebar.write(w3.eth.get_balance(os.getenv("SMART_CONTRACT_ADDRESS")))

# Mint Tokens Fuunction (Checks to make sure the account calling the function has the minter role, 
# then executes. otherwise an error will raise)
st.write("Mint Tokens:")
tokens_to_mint = st.number_input("Tokens to Mint", value = 0)
if st.button("Mint"):
    if contract.caller.hasRole(contract.caller.MINTER_ROLE(),
     address) == True:
      tx_hash = contract.functions.mint(address,tokens_to_mint).transact({'from': address, 'gas': 1000000})
      receipt = w3.eth.waitForTransactionReceipt(tx_hash)
      st.write("Transaction receipt mined:")
      st.write(dict(receipt))

    else:
      st.write("you do not have permission to mint tokens")
    
st.write("Buy_Tokens")
tokens_to_buy = st.number_input("Tokens to Buy", value = 0)
if st.button("Buy RCS Tokens"):
      tx_hash = contract.functions.buy().transact({'from': address, 'gas': 1000000, 'value': tokens_to_buy})
      receipt = w3.eth.waitForTransactionReceipt(tx_hash)
      st.write("Transaction receipt mined:")
      st.write(dict(receipt))

st.markdown("---")


