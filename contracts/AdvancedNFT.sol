// We are going to give a random NFT to the msg sender
// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedNFT is VRFConsumerBase, ERC721 {
    uint256 public tokenCounter;
    bytes32 public keyHash;
    uint256 public fees;
    enum shipPics {
        Old,
        New,
        Fighter
    }
    mapping(bytes32 => address) public requestToSender;
    mapping(uint256 => shipPics) public tokenIDToShip;

    // It's a good practice to emit events whenever the mapping is being updated.
    event requestedCollectible(bytes32 indexed requestedID, address requester);
    event shipAssigned(uint256 indexed tokenId, shipPics SP);

    constructor(
        address _vrfCoordinator,
        address _link,
        bytes32 _keyHash,
        uint256 _fees
    ) public VRFConsumerBase(_vrfCoordinator, _link) ERC721("Ships", "SHS") {
        tokenCounter = 0;
        keyHash = _keyHash;
        fees = _fees;
    }

    function NFTCreation() public returns (bytes32) {
        bytes32 requestID = requestRandomness(keyHash, fees);
        requestToSender[requestID] = msg.sender;
        emit requestedCollectible(requestID, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        shipPics SP = shipPics(randomNumber % 3);
        uint256 tokenId = tokenCounter;
        tokenIDToShip[tokenId] = SP;
        emit shipAssigned(tokenId, SP);
        //Coz the caller of this function will not be the one who requested randomness but the
        //one who is sending the randomness
        address owner = requestToSender[requestId];
        _safeMint(owner, tokenId);
        tokenCounter += 1;
    }

    function setTokenURI(uint256 tokenId, string memory tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not the owner or not approced."
        );
        _setTokenURI(tokenId, tokenURI);
    }
}
