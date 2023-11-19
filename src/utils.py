import json

import requests
import logging

from src.class_ import Albums


# logger = logging.getLogger(__name__)


def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # logger.error(f"Failed to receive data. Status code: {response.status_code}")
        return None


def save_data_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
        # logger.info("Data saved to file")


def get_info_from_json_file(filename) -> list[dict]:
    """открывает файл о словарями в формате json и превращает в формат питон"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def sort_album_by_id(all_pictures, album_id):
    return [picture for picture in all_pictures if picture['albumId'] == album_id]


def get_operation_instances(albums):
    list_ = []
    for album in albums:
        if album:
            list_.append(
                Albums(
                    album_id=album["albumId"],
                    id_number=album["id"],
                    title=album["title"],
                    url=album["url"],
                    thumbnail_url=album["thumbnailUrl"]
                )
            )
    return list_

# INFO:root:Starting app...
# INFO:root:Downloading album 1 images...
# INFO:root:Saving image 1 to photos/1-1.jpg
# INFO:root:Saving image 2 to photos/1-2.jpg
# INFO:root:Saving image 3 to photos/1-3.jpg
# INFO:root:Saving image 4 to photos/1-4.jpg
# INFO:root:Saving image 5 to photos/1-5.jpg
# INFO:root:Finished downloading images. Total images downloaded: 5

# import requests
# from pathlib import Path
#
#
# number = 2
# data_path = Path(Path(__file__).parent.parent.joinpath('data', 'photos', f'1-{number}.png'))
# data_path.parent.mkdir(exist_ok=True, parents=True)
# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open(data_path, 'wb') as f:
#     f.write(r.content)