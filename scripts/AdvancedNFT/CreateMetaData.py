import json
from brownie import AdvancedNFT, network
from ..helpfulScripts import getShipType, uploadIPFS
from pathlib import Path
from metadata.sampleMetaData import metadata_template

URIMapping = {"": ""}


def main():
    advanced_collectible = AdvancedNFT[-1]
    numberOfTokensSupplied = advanced_collectible.tokenCounter()
    print(f"There have been {numberOfTokensSupplied} collectibles created.")
    for tokenId in range(numberOfTokensSupplied):
        shipType = getShipType(advanced_collectible.tokenIDToShip(tokenId))
        metadata_file = f"./metadata/{network.show_active()}/{tokenId}-{shipType}.json"
        NFTMetadata = metadata_template
        # To check whether the file already exists or not.
        if Path(metadata_file).exists():
            print(f"{metadata_file} already exits! Delete file to overwrite.")
        else:
            print(f"Creating file -> {metadata_file}")
            # Changing the data of the metadsta
            imagePath = "./images/" + shipType.lower() + ".png"
            NFTMetadata["name"] = f"{shipType} Ship"
            NFTMetadata["description"] = f"A beautiful {shipType} ship"
            imageURI = uploadIPFS(imagePath)
            NFTMetadata["image"] = imageURI
            with open(metadata_file, "w") as file:
                json.dump(NFTMetadata, file)
            URI = uploadIPFS(metadata_file)
            addToURIMapping(shipType, URI)


def addToURIMapping(shipType, URI):
    URIMapping[URI] = shipType
