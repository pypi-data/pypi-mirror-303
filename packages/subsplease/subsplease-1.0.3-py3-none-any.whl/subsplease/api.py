from typing import Generator
from rich import print
import httpx
from .models import Episode
from .constants import EndPoints


class SubsPlease:
    def __init__(self, timezone: str = "Asia/Calcutta") -> None:
        self.timezone = timezone
        self.session = httpx.Client(timeout=60)

    def search(self, query: str) -> Generator[Episode, None, None]:
        response = self.session.get(
            EndPoints.SEARCH_ENDPOINT,
            params={
                "s": query,
                "tz": self.timezone,
            },
        )

        if response.status_code == 200:
            data = response.json()
            for _, episode_info in data.items():
                yield Episode.create(episode_info)
        else:
            print("Error:", response.status_code)
            print("Error JSON:", response.json())
