from brownie import network, config, accounts

OPENSEA_URL = 'https://testnets.opensea.io/assets/{}/{}' if network.show_active() == "rinkeby" else 'https://opensea.io/assets/{}/{}'
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache", "mainnet-fork"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])