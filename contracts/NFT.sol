// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NFT is ERC721 {
    uint256 public tokenCounter;
    
    constructor (string memory _name, string memory _symbol) public ERC721 (_name, _symbol){
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI) public returns (uint256){
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newTokenId;
    }
}
