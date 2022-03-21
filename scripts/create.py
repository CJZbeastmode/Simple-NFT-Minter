from brownie import NFT, network
from pathlib import Path
import requests
import json
from scripts.sample_metadata import metadata_template
from config import TOKEN_NAME, TOKEN_DESCRIPTION, TOKEN_IMAGE_NAME, IPFS_URL
from scripts.helpful_scripts import OPENSEA_URL, get_account

def create_metadata():
    # Get Token ID
    nft = NFT[-1]
    token_id = nft.tokenCounter()
    # Set up Metadata File
    metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{TOKEN_NAME}.json"
    nft_metadata = metadata_template
    print(f"Creating Metadata file: {metadata_file_name}")
    # Set up Image Field
    image_path = f"./img/{TOKEN_IMAGE_NAME}"
    image_uri = upload_to_ipfs(image_path)
    nft_metadata["image"] = image_uri
    # Set up Name
    nft_metadata["name"] = TOKEN_NAME
    # Set up Description
    nft_metadata["description"] = TOKEN_DESCRIPTION
    # Dump into JSON File
    with open(metadata_file_name, "w") as file:
        json.dump(nft_metadata, file)
    # Upload File
    json_uri = upload_to_ipfs(metadata_file_name)
    # Return
    return json_uri

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = IPFS_URL
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-NFT.png" -> "0-NFT.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print("Uploaded File URL: " + image_uri)
        return image_uri

def create_token():
    json_uri = create_metadata()
    account = get_account()
    tx = NFT[-1].createCollectible(json_uri, {'from': account})
    tx.wait(1)
    if network.show_active() == "rinkeby" or network.show_active() == "mainnet": 
        print(f"NFT Created! You can now view your NFT at {OPENSEA_URL.format(NFT[-1].address, NFT[-1].tokenCounter() - 1)}")
    else:
        print(f"NFT Created! The contract address is {NFT[-1].address} and the token ID is {NFT[-1].tokenCounter() - 1}")
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")

def main():
    create_token()