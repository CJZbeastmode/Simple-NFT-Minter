from brownie import NFT
from config import TOKEN_NAME, TOKEN_SYMBOL_NAME
from scripts.helpful_scripts import get_account

def deploy():
    account = get_account()
    token = NFT.deploy(TOKEN_NAME, TOKEN_SYMBOL_NAME, {'from': account})
    print("Contract deployed!")
    return token

def main():
    deploy()  