from enum import Enum
from .flag import Flag
from .table import Table, TableFromArray, Search
from .types import INTEGER, STRING, ListOf, JoinedStrings
from .common import Gender, SpoilerLevel, ImageFlagging

class BloodType(Enum):
    A = 'a'
    B = 'b'
    AB = 'ab'
    O = 'o'

class Role(Enum):
    MAIN = 'main'
    PRIMARY = 'primary'
    SIDE = 'side'
    APPEARS = 'appears'

none = Flag.NONE

class Birthday(TableFromArray):
    day = none.Column(INTEGER)
    month = none.Column(INTEGER)

class CharacterTrait(TableFromArray):
    id = none.Column(INTEGER)
    spoiler_level = none.Column(SpoilerLevel)

class CharacterAppearance(TableFromArray):
    vn_id = none.Column(INTEGER)
    release_id = none.Column(INTEGER)
    spoiler_level = none.Column(SpoilerLevel)
    role = none.Column(Role)

class CharacterVoiced(Table):
    staff_id = none.Column(INTEGER).with_name('id')
    staff_alias_id = none.Column(INTEGER).with_name('aid')
    vn_id = none.Column(INTEGER).with_name('vid')
    note = none.Column(STRING)

class CharacterInstance(Table):
    id = none.Column(INTEGER)
    spoiler_level = none.Column(SpoilerLevel).with_name('spoiler')
    name = none.Column(STRING)
    original_name = none.Column(STRING).with_name('original')

basic = Flag.BASIC
details = Flag.DETAILS
meas = Flag.MEASURES
traits = Flag.TRAITS
vns = Flag.VNS
voiced = Flag.VOICED
instances = Flag.INSTANCES

class Character(Table):
    id = none.Column(INTEGER)
    name = basic.Column(STRING)
    original_name = basic.Column(STRING).with_name('original')
    gender = basic.Column(Gender)
    spoil_gender = basic.Column(Gender)
    blood_type = basic.Column(BloodType).with_name('bloodt')
    birthday = basic.Column(Birthday)
    aliases = details.Column(JoinedStrings())
    description = details.Column(STRING)
    age = details.Column(INTEGER)
    image = details.Column(STRING)
    image_flagging = details.Column(ImageFlagging)
    image_width = details.Column(INTEGER)
    image_height = details.Column(INTEGER)
    bust = meas.Column(INTEGER)
    waist = meas.Column(INTEGER)
    hip = meas.Column(INTEGER)
    height = meas.Column(INTEGER)
    weight = meas.Column(INTEGER)
    cup_size = meas.Column(STRING)
    traits = traits.Column(ListOf(CharacterTrait))
    vns = vns.Column(ListOf(CharacterAppearance))
    voiced = voiced.Column(ListOf(CharacterVoiced))
    instances = instances.Column(ListOf(CharacterInstance))

    search = Search()
    vn_id = Search().with_name('vn')
