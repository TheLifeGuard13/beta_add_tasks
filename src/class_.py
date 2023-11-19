from pathlib import Path

import requests


class Albums:
    def __init__(self, album_id: int, id_number: int, title: str, url: str, thumbnail_url: str):
        self.album_id = album_id
        self.id_number = id_number
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    def load_picture(self) -> None:
        """скачивает картинку по ссылке и сохраняет в формате png."""
        data_path = Path(
            Path(__file__).parent.parent.joinpath("data", "photos", f"{self.album_id}-{self.id_number}.png")
        )
        data_path.parent.mkdir(exist_ok=True, parents=True)
        r = requests.get(self.url)
        with open(data_path, "wb") as f:
            f.write(r.content)

    def __repr__(self) -> str:
        return f"""Albums(album_id={self.album_id}, id_number={self.id_number},
        title={self.title}, url={self.url}, thumbnail_url={self.thumbnail_url})"""
