# Simple NFT Minter
!!!: MINTING NFT ON RINKEBY TESTNET BEFORE WORKING WITH ETHEREUM MAINNET AND ACTUAL MONEY IS STRONGLY RECOMMENEDED!

This repository enables users to mint their own NFTs in a local environment (ganache), on an ethereum testnet (rinkeby) or on the ethereum mainnet.



## Install
```
git clone https://github.com/CJZbeastmode/Simple-NFT-Minter
```



## Usage
An NFT (Non-Fungible Token) is a smart contract with ERC721 standard stored on a specific contract address on the Ethereum blockchain with a token ID. Every NFT can be viewed on Opensea using the URL pattern https://opensea.io/assets/{contract_address}/{token_id} for mainnet and https://testnets.opensea.io/assets/{contract_address}/{token_id} for rinkeby.

Preparation:<br />
1, Enabling IPFS
```
ipfs daemon
```
*: The installing process of IPFS is listed below

2, Redirecting to this repository in a local environment using terminal or command prompt

3, Make sure there are enough funds in your wallet
    -- for rinkeby network, request funds using a rinkeby faucet (https://faucets.chain.link/rinkeby)
    -- for mainnet network, purchase ethereum on an authorized cryptocurrency site
    -- for development network, make sure that ganache-cli is installed and works properly
    
4, Set up environment variables in .env file
    -- In order to use this repository, you need to set up a .env file which consists of all environment variables. Create a .env file in the root of the directory, copy the file content in env_file_example.md and fill all the keys required. Details about keys can be found in the section "required keys".

The process of minting NFT consists of two phases:<br />
1, Deploying Contract
Deploying a contract means creating an NFT collection and bringing it onto the blockchain.

Rinkeby:
```
brownie run scripts/deploy.py --network rinkeby
```

Mainnet:
```
brownie run scripts/deploy.py --network mainnet
```

Development:
```
brownie run scripts/deploy.py
```

The output on the command line will render the address in which the smart contract is deployed. You can use Etherscan (for rinkeby: https://rinkeby.etherscan.io/; for mainnet: https://etherscan.io/) to check whether the smart contract is correctly deployed.

2, Creating Tokens<br />
Creating a token on the latest contract deployed. Make sure that the config file is set!

Rinkeby:
```
brownie run scripts/create.py --network rinkeby
```

Mainnet:
```
brownie run scripts/create.py --network mainnet
```

Development:
```
bronwie run scripts/create.py
```

The output on the command line will render the IPFS address in which the metadata files are uploaded. If you deployed your NFT on rinkeby or mainnet, you can view your newly created NFT on Opensea. The address of the Opensea will be rendered on the command line. Make sure to wait up to 20 minutes and click the "refresh metadata" button on the Opensea web page, since Opensea needs a couple minutes to fully update its metadata files.



## Configurations
1, Config File<br />
The config file is a file containing the information of the next NFT that you want to mint and the URL of IPFS.
TOKEN_NAME: The name of the NFT that you want to create
TOKEN_SYMBOL_NAME: The name abbreviation of the NFT that you want to create
TOKEN_DESCRIPTION: The description of the NFT that you want to create
TOKEN_IMAGE_NAME: The exact image name of the NFT that you want to create (The image must be stored in the "img" folder)
TOKEN_ATTRIBUTES: The attributes of the NFT that you want to create (Format is listed in the config file. Please keep the data consistent!)
IPFS_URL: The URL of your local IPFS environment. The default address (if not changed) is http://127.0.0.1:5001

2, Image<br />
Before creating a new token please keep the image in the img file and make sure the TOKEN_IMAGE_NAME field in the config file is identical to the image file name in the img folder. The image will then be uploaded to IPFS and filled into the metadata file, so that Opensea can recognize the image and correctly render it.


## Wallet
In order to deploy contracts and create NFT tokens on a blockchain testnet or mainnet, a crypto wallet is required. Metamask is strongly recommended, as it is easy to install and easy to use.<br />
To download metamask and create an account, follow this link: https://metamask.io/download/<br />
To request funds into your rinkeby account, use this rinkeby faucet: https://faucets.chain.link/rinkeby <br />
To purchase Ethereum, use an authorized cryptocurrency vendering site like Coinbase (https://www.coinbase.com/)<br />


## Required Dependencies
1, Python 3.8<br />
This repository interacts with the Ethereum blockchain with Python. Make sure that Python ***3.8 (VERY IMPORTANT!!!)*** is installed on your local environment.  
Download Python 3.8: https://www.python.org/ (Information about Operating Systems can be found on the website)

2, Brownie<br />
The scripts of this repository are written to be compiled and run by brownie, a framework for blockchain development. 
Download Brownie: https://github.com/eth-brownie/brownie

3, IPFS<br />
The Simple NFT Minter uses IPFS as storage of metadata files. IPFS is a decentralized storage with cutting-edge technology. 
Dowload IPFS: http://docs.ipfs.io.ipns.localhost:8080/install/command-line/#system-requirements

4, ganache-cli<br />
The Simple NFT Minter requires ganache-cli (command line Ganache) if you want to mint your NFT on a local blockchain. You can download ganache using ganache-cli
```
npm install -g ganache-cli
```



## Required Keys
-- Wallet Private Key<br />
Using this Repository requires the private key of the wallet. Open your wallet, find the private key of your account and paste it to the PRIVATE_KEY variable in the .env file.


-- Infura Project ID<br />
Using this Repository requires an Infura Project ID. An Infura Project ID can be acquired as follow:<br />
1, Visit https://infura.io/<br />
2, Sign up for Infura
![alt text](/README_img/Infura/SignUp.png)
3, Create New Project
![alt text](/README_img/Infura/CreateNewProject.png)
4, Fill out the Fields and Save (Select Ethereum in the Top Field)
![alt text](/README_img/Infura/ProjectInfo.png)
5, Copy the Project ID and Paste it to the .env File 
![alt text](/README_img/Infura/Dashboard.png)

-- Github API Token<br />
Using this Repository requires the a Github API Token. A Github API Token can be acquired as follows:<br />
1, Visit https://github.com/
![alt text](/README_img/Github/Homepage.png)
2, Sign up for Github
![alt text](/README_img/Github/SignUp.png)
3, Click Settings on your Github Dashboard
![alt text](/README_img/Github/Dashboard.png)
4, Scroll to the bottom of Settings and Click Developer Settings
![alt text](/README_img/Github/Settings.png)
5, Click Personal Access Tokens on the Sidebar of Developer Settings
![alt text](/README_img/Github/DevSettings.png)
6, Click Generate New Token
![alt text](/README_img/Github/Tokens.png)
7, Fill in the Fields
![alt text](/README_img/Github/CreateToken.png)
8, Copy the API Token and Paste it to the .env File
![alt text](/README_img/Github/Info.png)



## Contact
Chengjie (Jay) Zhou<br />

Github: https://www.github.com/CJZbeastmode<br />
Twitter: https://twitter.com/chou_cj<br />
Instagram: https://www.instagram.com/cjz_beastmode/<br />
Email: jay0816@outlook.com<br />
Ethereum Wallet Address: 0x3221A67F25507812A16664f191F030b247d17773



## Links
Test Image: https://www.zwentner.com/rickroll-url-shortener/
