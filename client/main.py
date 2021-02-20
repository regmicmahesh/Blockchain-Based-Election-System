import json
from web3 import Web3

abi = []
sub_abi = []

with open("majorAuthority.json") as jsonFile:
    abi = json.load(jsonFile)["abi"]

with open("subAuthority.json") as jsonFile:
    sub_abi = json.load(jsonFile)["abi"]


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

contract = w3.eth.contract(address="0x2cc9B5C2b0AaAd51cA8EF4a5e114C330693BA392", abi=abi)
subauthority = w3.eth.contract(address="0x1e1833D0FFB5a94FBc8B587d13aE299018003239", abi=sub_abi)

# w3.eth.sendTransaction()

# w3.eth.sendTransaction({"from":"", "to" : "", value: Web3.toWei(1)})