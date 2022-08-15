from fileinput import filename
from urllib import response
from brownie import config, accounts, network, LinkToken, VRFCoordinatorMock, Contract
from pathlib import Path
import requests

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-cli"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
contractToMock = {"link": LinkToken, "vrf-coordinator": VRFCoordinatorMock}
shipMapping = {0: "Old", 1: "New", 2: "Fighter"}


def getShipType(shipNumber):
    return shipMapping[shipNumber]


def getAccount(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        and network.show_active() not in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts.add(config["wallets"]["from-key"])
    else:
        return accounts[0]


def getContract(contract_name):
    contract_type = contractToMock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deployMocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deployMocks():
    print("Deploying Mocks...")
    account = getAccount()
    linkDC = LinkToken.deploy({"from": account})
    VRFCoordinatorMock.deploy(linkDC, {"from": account})
    print("Mocks Deployed")


def fund_with_link(
    contractAddress, account=None, linkToken=None, amount=100000000000000000
):
    account = account if account else getAccount()
    linkToken = linkToken if linkToken else getContract("link")
    tx = linkToken.transfer(contractAddress, amount, {"from": account})
    tx.wait(1)
    return tx


def uploadIPFS(imagePath):
    # Now we have to open the image in binary
    with Path(imagePath).open("rb") as fp:
        image_binary = fp.read()
        ipfsURL = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfsURL + endpoint, files={"file": image_binary})
        imageHash = response.json()["Hash"]
        # /images/0-Old.png -> 0-Old.png
        filename = imagePath.split("/")[-1:][0]
        imageURI = f"https://ipfs.io/ipfs/{imageHash}/filename={filename}"
        print(imageURI)
        return imageURI
