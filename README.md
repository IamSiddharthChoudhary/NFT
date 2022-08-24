Advanced NFT:
- In this, the user will get a ramdom NFT among the three (which are here the pics of ships). 
- And this randomness is attained by using VRF(Verifiable random function) of chainlink.
- Also here we are uploading our inages and their json file to IPFS(Inter Planetary File System).
- And this IPFS link is then deployed to bloackchain.

Story:-
- Firstly, we created a simpleNFT contract to get started and in this 
  we took file URI of the image directly from pinata.
- Then we created Advanced NFT.

Demerits of SimpleNFT:
1. We didn't upload our image to IPFS ourselves.
2. Anyone can mint NFTs here as they are not verifiably random or scare.

To Overcome them we will created Advanced NFT contract in contracts folder.


