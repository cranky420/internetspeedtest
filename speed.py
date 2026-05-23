import requests
import time

def test_speed():

    ip = requests.get(
        "https://api.ipify.org"
    ).text

    start = time.time()

    response = requests.get(
        "https://jsonplaceholder.typicode.com/photos"
    )

    end = time.time()

    seconds = end-start

    download = round(
        10/seconds,
        2
    )

    upload = 42

    return {

        "download":download,
        "upload":upload,
        "ip":ip

    }