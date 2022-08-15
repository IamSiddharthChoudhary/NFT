from brownie import AdvancedNFT
from scripts.helpfulScripts import getShipType, set_TokenURI
from scripts.AdvancedNFT.CreateMetaData import URIMapping


def main():
    advancedCollectible = AdvancedNFT[-1]
    numberOfCollectibles = advancedCollectible.tokenCounter()
    print(f"You've got {numberOfCollectibles} collectibles")
    for tokenId in range(numberOfCollectibles):
        shipType = getShipType(advancedCollectible.tokenIDToShip(tokenId))
        if not advancedCollectible.tokenURI(tokenId).startwith("https:/"):
            print(f"Setting tokenURI of {tokenId}")
            set_TokenURI(tokenId, advancedCollectible, URIMapping[shipType])
