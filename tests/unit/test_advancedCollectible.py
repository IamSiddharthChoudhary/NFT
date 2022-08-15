from brownie import network
from scripts.AdvancedNFT.CreateCollectible import CreateCollectible
from scripts.AdvancedNFT.deploy import deployNFT
from scripts.helpfulScripts import (
    getAccount,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    getContract,
)
import pytest


def test_advancedCollectible():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local network")
    # Act
    collectible, creationTx = deployNFT()
    requestId = creationTx.events["requestedCollectible"]["requestedID"]
    vrfCoordinator = getContract("vrf-coordinator")
    randomNumber = 43
    vrfCoordinator.callBackWithRandomness(requestId, randomNumber, collectible.address)
    # Assert
    assert collectible.tokenCounter() == 1
    assert collectible.tokenIDToShip(0) == randomNumber % 3
