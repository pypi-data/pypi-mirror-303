from typing import Any
from datetime import datetime
from dataclasses import dataclass
from .enums import Quality
from .constants import EndPoints


def create_quality(text: str) -> Quality:
    try:
        return Quality(f"{text}p")
    except ValueError:
        raise ValueError(
            f"Invalid quality '{text}'. Must be one of: {[quality.value for quality in Quality]}"
        )


@dataclass
class Download:
    quality: Quality
    magnet: str

    def __repr__(self) -> str:
        return f"Download(quality={self.quality}, magnet={self.magnet[:10]}...)"

    @staticmethod
    def create(raw_data: dict[str, Any]) -> "Download":
        return Download(
            quality=create_quality(raw_data["res"]),
            magnet=raw_data["magnet"],
        )


@dataclass
class Episode:
    show: str
    episode: int
    release_date: datetime
    downloads: list[Download]
    xdcc: str
    image_url: str
    page: str

    @staticmethod
    def create(raw_data: dict[str, Any]) -> "Episode":
        downloads = [Download.create(download) for download in raw_data["downloads"]]
        return Episode(
            show=raw_data["show"],
            episode=raw_data["episode"],
            release_date=datetime.strptime(
                raw_data["release_date"], "%a, %d %b %Y %H:%M:%S %z"
            ),
            downloads=downloads,
            xdcc=raw_data["xdcc"],
            image_url=raw_data["image_url"],
            page=f'{EndPoints.BASE_URL}/{raw_data["page"]}',
        )
