from .flag import Flag
from .table import Table
from .types import INTEGER

none = Flag.NONE

class DBStats(Table):
    tags = none.Column(INTEGER)
    releases = none.Column(INTEGER)
    producers = none.Column(INTEGER)
    characters = none.Column(INTEGER).with_name('chars')
    vns = none.Column(INTEGER).with_name('vn')
    traits = none.Column(INTEGER)
