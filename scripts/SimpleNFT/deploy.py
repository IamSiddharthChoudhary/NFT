from lib2to3.pgen2 import token
from brownie import SimpleNFT
from scripts.helpfulScripts import getAccount, OPENSEA_URL

URI_IPFS = "ipfs://QmXBx4ZLDD7bhAwhveqgCikRCPLxZPxLREdfiLqxiP2nWf/shp.json"


def main():
    deployNFT()


def deployNFT():
    account = getAccount()
    NFT = SimpleNFT.deploy({"from": account})
    tx = NFT.createSimpleNFT(URI_IPFS, {"from": account})
    tx.wait(1)
    print(f"You can view your NFT at {OPENSEA_URL.format(NFT.address,NFT.tokenIndex)}")
    print("Please wait upto 20 minutes, and hit refresh metadata button.")
    return NFT
