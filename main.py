from plate_finder_client import get_plate_text, is_foreign_plate
from scrapper import Scrapper
from time import sleep
from progress.bar import Bar

IMAGE_URL = "https://i.simpalsmedia.com/999.md/BoardImages/900x900/72c23bc2c8f7d50cdeb29a3d68ae1851.jpg"
scrapper = Scrapper()
scrapper.find_images()
ads_count = len(scrapper.ads_list)

with Bar('Processing...', max=ads_count, suffix='%(percent).1f%% - %(eta)ds') as bar:
    for i in range(ads_count):
        sleep(0.02)
        bar.next()
        plate_num = get_plate_text(scrapper.ads_list[i].img_url)
        if is_foreign_plate(plate_num):
            print(f'Ad found: {scrapper.ads_list[i].ad_url}')
