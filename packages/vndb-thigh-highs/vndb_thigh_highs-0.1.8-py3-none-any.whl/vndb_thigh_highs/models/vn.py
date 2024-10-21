from enum import Enum
from .flag import Flag
from .table import Table, TableFromArray, Search
from .types import (
    BOOLEAN, DATE, INTEGER, FLOAT, STRING,
    ListOf, JoinedStrings, FirstElementOf)
from .common import SpoilerLevel, ImageFlagging

class Length(Enum):
    VERY_SHORT = 1
    SHORT = 2
    MEDIUM = 3
    LONG = 4
    VERY_LONG = 5

none = Flag.NONE

class Title(Table):
    language = none.Column(STRING).with_name('lang')
    title = none.Column(STRING).with_name('latin')
    original_title = none.Column(STRING).with_name('title')
    official = none.Column(BOOLEAN)

class VNTag(TableFromArray):
    tag_id = none.Column(INTEGER)
    score = none.Column(FLOAT)
    spoiler_level = none.Column(SpoilerLevel)

class Links(Table):
    wikidata = none.Column(STRING)
    renai = none.Column(STRING)

class Anime(Table):
    anidb_id = none.Column(INTEGER).with_name('id')
    ann_id = none.Column(INTEGER)
    nfo_id = none.Column(INTEGER)
    title_romaji = none.Column(STRING)
    title_kanji = none.Column(STRING)
    year = none.Column(INTEGER)
    type = none.Column(STRING)

class VNRelation(Table):
    id = none.Column(INTEGER)
    relation = none.Column(STRING)
    title = none.Column(STRING)
    original_title = none.Column(STRING).with_name('original')
    official = none.Column(BOOLEAN)

class Screenshot(Table):
    id = none.Column(STRING)
    image = none.Column(STRING)
    release_id = none.Column(INTEGER).with_name('rid')
    flagging = none.Column(ImageFlagging)
    width = none.Column(INTEGER)
    height = none.Column(INTEGER)
    thumbnail = none.Column(STRING)
    thumbnail_width = none.Column(INTEGER)
    thumbnail_height = none.Column(INTEGER)

class VNStaff(Table):
    staff_id = none.Column(INTEGER).with_name('sid')
    staff_alias_id = none.Column(INTEGER).with_name('aid')
    name = none.Column(STRING)
    original_name = none.Column(STRING).with_name('original')
    role = none.Column(STRING)
    note = none.Column(STRING)

basic = Flag.BASIC
details = Flag.DETAILS
titles = Flag.TITLES
anime = Flag.ANIME
relations = Flag.RELATIONS
tags = Flag.TAGS
stats = Flag.STATS
screens = Flag.SCREENS
staff = Flag.STAFF

class VN(Table):
    id = none.Column(INTEGER)
    title = basic.Column(STRING)
    original_title = basic.Column(STRING).with_name('original')
    released_date = basic.Column(DATE).with_name('released')
    languages = basic.Column(ListOf(STRING))
    original_language = basic.Column(FirstElementOf(ListOf(STRING))).with_name('orig_lang')
    platforms = basic.Column(ListOf(STRING))
    aliases = details.Column(JoinedStrings())
    length = details.Column(Length)
    length_in_minutes = details.Column(INTEGER).with_name('length_minutes')
    length_vote_count = details.Column(INTEGER).with_name('length_votes')
    description = details.Column(STRING)
    links = details.Column(Links)
    image = details.Column(STRING)
    image_flagging = details.Column(ImageFlagging)
    image_width = details.Column(INTEGER)
    image_height = details.Column(INTEGER)
    titles = titles.Column(ListOf(Title))
    anime = anime.Column(ListOf(Anime))
    relations = relations.Column(ListOf(VNRelation))
    tags = tags.Column(ListOf(VNTag))
    rating = stats.Column(FLOAT)
    vote_count = stats.Column(INTEGER).with_name('votecount')
    screens = screens.Column(ListOf(Screenshot))
    staff = staff.Column(ListOf(VNStaff))

    search = Search()
    firstchar = Search()
