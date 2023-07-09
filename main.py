from plate_finder_client import get_plate_text, is_foreign_plate
from scrapper import Scrapper

IMAGE_URL = "https://i.simpalsmedia.com/999.md/BoardImages/900x900/72c23bc2c8f7d50cdeb29a3d68ae1851.jpg"
scrapper = Scrapper()
scrapper.find_images()

for ad in scrapper.ads_list:
    plate_num = get_plate_text(ad.img_url)
    if is_foreign_plate(plate_num):
        print(f'Ad found: {ad.ad_url}')

