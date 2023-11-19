from src.logger import setup_logging
from src.utils import get_data_from_api, get_operation_instances, sort_album_by_id

logger = setup_logging()


def main(album_id: int, limit: int = 100) -> None:
    logger.info("Starting app...")
    url = "https://jsonplaceholder.typicode.com/photos"

    logger.info(f"Downloading album {album_id} images...")

    # скачиваем данные по ссылке в формате json
    data = get_data_from_api(url)

    # выбираем выбранный альбом и выбранное количество картинок
    picked_album_id = sort_album_by_id(data, album_id)[:limit]

    # складываем выбранные картинки в экземпляры класса
    pictures_instances = get_operation_instances(picked_album_id)

    for picture in pictures_instances:
        logger.info(f"Saving image {picture.id_number} to photos/{picture.album_id}-{picture.id_number}.png")
        # обращаемся к методу класса - сохранение картинки экземлпяра в файл
        picture.load_picture()
    logger.info(f"Finished downloading images. Total images downloaded: {len(picked_album_id)}")


if __name__ == "__main__":
    main(1, 3)
