import imp
from brownie import network
from scripts.helpfulScripts import getAccount, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.SimpleNFT.deploy import deployNFT
import pytest


def test_can_create_NFT():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    NFT = deployNFT()
    assert NFT.ownerOf(0) == getAccount(0)
