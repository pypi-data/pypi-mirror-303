from enum import Enum
from .table import ColumnBuilder

class Flag(Enum):
    BASIC = "basic"
    DETAILS = "details"
    TITLES = "titles"
    ANIME = "anime"
    RELATIONS = "relations"
    TAGS = "tags"
    STATS = "stats"
    SCREENS = "screens"
    STAFF = "staff"
    VN = "vn"
    LANGUAGES = "lang"
    PRODUCERS = "producers"
    LINKS = "links"
    MEASURES = "meas"
    TRAITS = "traits"
    VNS = "vns"
    VOICED = "voiced"
    INSTANCES = "instances"
    ALIASES = "aliases"
    LABELS = "labels"

    NONE = None

    def __str__(self):
        return self.value

    def __lt__(self, other):
        return self.value < other.value

    def Column(self, field_constructor):
        return ColumnBuilder(field_constructor, self)
