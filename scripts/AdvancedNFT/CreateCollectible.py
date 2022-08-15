from scripts.helpfulScripts import getAccount, fund_with_link
from brownie import AdvancedNFT
from web3 import Web3


def CreateCollectible():
    account = getAccount()
    contract = AdvancedNFT[-1]
    fund_with_link(contract.address, amount=Web3.toWei(0.1, "ether"))
    contractTx = contract.NFTCreation({"from": account})
    contractTx.wait(1)
    return contractTx


def main():
    CreateCollectible()
