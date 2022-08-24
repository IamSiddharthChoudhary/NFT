from brownie import AdvancedNFT, network
from scripts.helpfulScripts import getAccount, OPENSEA_URL, getContract, fund_with_link


def deployNFT():
    account = getAccount()
    NFT = AdvancedNFT.deploy(
        getContract("vrf-coordinator"),
        getContract("link"),
        "0x2ed0feb3e7fd2022120aa84fab1945545a9f2ffc9076fd6156fa96eaff4c1311",
        100000000000000000,
        {"from": account},
    )
    print(type(NFT))
    fund_with_link(NFT.address)
    createCollectible = NFT.NFTCreation({"from": account})
    createCollectible.wait(1)
    print(type(createCollectible))
    return NFT, createCollectible


def main():
    deployNFT()
