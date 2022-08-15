// SPDX-License-Identifier:MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleNFT is ERC721 {
    uint256 public tokenIndex;

    constructor() public ERC721("Ship", "SHP") {
        tokenIndex = 0;
    }

    function createSimpleNFT(string memory tokenURI) public returns (uint256) {
        uint256 tokenID = tokenIndex;
        _safeMint(msg.sender, tokenIndex);
        _setTokenURI(tokenID, tokenURI);
        tokenIndex += 1;
        return tokenID;
    }
}
