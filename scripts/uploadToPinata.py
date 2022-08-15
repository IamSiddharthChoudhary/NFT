# Only for backup we are uploading it to IPFS through Pinata

from fileinput import filename
import os
from pathlib import Path
import requests

PINATA_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"

header = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET_KEY"),
}
filePath = "./images/new.png"
fileName = filePath.split("/")[-1:][0]


def main():
    with Path(filePath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_URL + endpoint,
            files={"file": (fileName, image_binary)},
            headers=header,
        )
        print(response.json())
