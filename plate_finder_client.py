import requests
from urllib.request import urlopen
from urllib.error import HTTPError
import re

LOCAL_HOST = 'http://localhost:5000/process'


def _upload_plate(img_url: str):
    with urlopen(img_url) as url:
        img_file = url.read()
    return requests.post(LOCAL_HOST, files={"image": img_file})


def get_plate_text(img_url: str):
    plate = ''
    try:
        res = _upload_plate(img_url).json()
        if res['ocr']:
            for el in res['ocr']:
                plate += el[0]
    except HTTPError:
        pass
    return plate


def is_foreign_plate(plate: str) -> bool:
    pattern = re.compile(r"[A-Za-z0-9]?[^hH]?H[0-9]+")
    return bool(pattern.match(plate))

