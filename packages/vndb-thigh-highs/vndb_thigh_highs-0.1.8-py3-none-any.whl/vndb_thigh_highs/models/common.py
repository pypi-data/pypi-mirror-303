from enum import Enum
from .table import Table
from .flag import Flag
from .types import INTEGER, FLOAT

class SpoilerLevel(Enum):
    NOT_A_SPOILER = 0
    MINOR_SPOILER = 1
    SPOILER = 2

class Gender(Enum):
    FEMALE = 'f'
    MALE = 'm'
    BOTH = 'b'
    UNKNOWN = 'unknown'

none = Flag.NONE

class ImageFlagging(Table):
    vote_count = none.Column(INTEGER).with_name('votecount')
    sexual_avg = none.Column(FLOAT)
    violence_avg = none.Column(FLOAT)
