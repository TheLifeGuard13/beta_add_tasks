import typing

import requests

from src.class_ import Albums


def get_data_from_api(url: str) -> typing.Any:
    """
    получает данные по ссылке и возвращает список словарей.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


def sort_album_by_id(all_pictures: list[dict], album_id: int) -> list[dict]:
    """
    сортирует список словарей по albumId
    """
    return [picture for picture in all_pictures if picture["albumId"] == album_id]


def get_operation_instances(albums: list[dict]) -> list[Albums]:
    """
    возвращает список экземпляров класса Albums
    """
    list_ = []
    for album in albums:
        if album:
            list_.append(
                Albums(
                    album_id=album["albumId"],
                    id_number=album["id"],
                    title=album["title"],
                    url=album["url"],
                    thumbnail_url=album["thumbnailUrl"],
                )
            )
    return list_
