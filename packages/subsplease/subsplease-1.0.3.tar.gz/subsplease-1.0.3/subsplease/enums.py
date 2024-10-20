from enum import Enum


class Quality(Enum):
    P480 = "480p"
    P720 = "720p"
    P1080 = "1080p"

    def __str__(self):
        return self.value
