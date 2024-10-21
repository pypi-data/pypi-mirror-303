from .flag import Flag
from .table import Table
from .types import INTEGER, STRING

none = Flag.NONE
basic = Flag.BASIC

class Quote(Table):
    vn_id = none.Column(INTEGER).with_name('id')
    vn_title = basic.Column(STRING).with_name('title')
    quote = basic.Column(STRING)

    random = 'random'
