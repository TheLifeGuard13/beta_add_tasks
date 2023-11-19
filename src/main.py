import json
import logging
from pathlib import Path

from src.utils import get_data_from_api, save_data_to_file, sort_album_by_id, get_info_from_json_file, \
    get_operation_instances


# Вам дан API https://jsonplaceholder.typicode.com/photos.
# Все шаги должны логироваться, от старта приложения,
# до вывода текущего состояния и информации о завершении приложения и общим количеством скачанных картинок.
#
# Требования к реализации:
#
# Все шаги приложения должны выводиться в консоль (использовать `logging`).
#
# Приложение должно принимать аргументы: `album_id` (обязательный) и `limit` (необязательный, по умолчанию 100).
#
# Приложение должно скачивать картинки по одной и выводить каждую в консоль
# с указанием имени файла и номером текущей картинки.
#
# В конце работы приложения должна выводиться информация о завершении работы и общем количестве скачанных картинок.

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# fh = logging.FileHandler('app.log', mode='w')
# fh.setLevel(logging.WARNING)
#
# formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
#
# logger.addHandler(ch)
# logger.addHandler(fh)


def main(album_id, limit=100):
    url = 'https://jsonplaceholder.typicode.com/photos'

    data = get_data_from_api(url)

    file_path = Path(__file__).parent.parent.joinpath('data', 'albums.json')
    save_data_to_file(file_path, data)

    all_albums = get_info_from_json_file(file_path)

    picked_album_id = sort_album_by_id(all_albums, album_id)[:limit]

    pictures_instances = get_operation_instances(picked_album_id)

    for picture in pictures_instances:
        print(picture.album_id, picture.id_number)
        picture.load_picture()


if __name__ == "__main__":
    main(1, 1)
