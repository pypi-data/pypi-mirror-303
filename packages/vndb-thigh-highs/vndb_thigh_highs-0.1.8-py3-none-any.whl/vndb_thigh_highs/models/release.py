from enum import Enum
from .flag import Flag
from .table import Table, TableFromArray, Search
from .types import BOOLEAN, DATE, INTEGER, STRING, ListOf

class ReleaseType(Enum):
    COMPLETE = 'complete'
    PARTIAL = 'partial'
    TRIAL = 'trial'

class Voiced(Enum):
    NOT_VOICED = 1
    ONLY_ERO_SCENES = 2
    PARTIAL = 3
    FULL = 4

class AnimationType(Enum):
    NO_ANIMATION = 1
    SIMPLE = 2
    SOME_SCENES = 3
    ALL_SCENES = 4

none = Flag.NONE

class Animation(TableFromArray):
    story = none.Column(AnimationType)
    ero = none.Column(AnimationType)

class Media(Table):
    medium = none.Column(STRING)
    quantity = none.Column(INTEGER).with_name('qty')

class ReleaseLanguage(Table):
    language = none.Column(STRING).with_name('lang')
    title = none.Column(STRING).with_name('latin')
    original_title = none.Column(STRING).with_name('title')
    machine_translation = none.Column(BOOLEAN).with_name('mtl')
    main = none.Column(BOOLEAN)

class ReleaseVN(Table):
    id = none.Column(INTEGER)
    title = none.Column(STRING)
    original_title = none.Column(STRING).with_name('original')
    release_type = none.Column(ReleaseType).with_name('rtype')

class ReleaseProducer(Table):
    id = none.Column(INTEGER)
    developer = none.Column(BOOLEAN)
    publisher = none.Column(BOOLEAN)
    name = none.Column(STRING)
    original_name = none.Column(STRING).with_name('original')
    type = none.Column(STRING)

class ReleaseLink(Table):
    label = none.Column(STRING)
    url = none.Column(STRING)

basic = Flag.BASIC
details = Flag.DETAILS
vn = Flag.VN
producers = Flag.PRODUCERS
links = Flag.LINKS

class Release(Table):
    id = none.Column(INTEGER)
    title = basic.Column(STRING)
    original_title = basic.Column(STRING).with_name('original')
    released_date = basic.Column(DATE).with_name('released')
    patch = basic.Column(BOOLEAN)
    freeware = basic.Column(BOOLEAN)
    languages = basic.Column(ListOf(STRING))
    website = details.Column(STRING)
    notes = details.Column(STRING)
    minimum_age = details.Column(INTEGER).with_name('minage')
    gtin = details.Column(STRING)
    catalog_number = details.Column(STRING).with_name('catalog')
    platforms = details.Column(ListOf(STRING))
    media = details.Column(ListOf(Media))
    resolution = details.Column(STRING)
    voiced = details.Column(Voiced)
    animation = details.Column(Animation)
    languages = Flag.LANGUAGES.Column(ListOf(ReleaseLanguage)).with_name('lang')
    vns = vn.Column(ListOf(ReleaseVN)).with_name('vn')
    producers = producers.Column(ListOf(ReleaseProducer))
    links = links.Column(ListOf(ReleaseLink))

    vn_id = Search().with_name('vn')
    producer_id = Search().with_name('producer')
