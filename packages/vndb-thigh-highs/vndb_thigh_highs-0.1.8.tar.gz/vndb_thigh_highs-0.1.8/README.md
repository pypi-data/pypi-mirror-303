# VNDB Thigh-highs
This module provides a VNDB client api implementation. It aims to provide some high level features to easily use VNDB api. It also includes some helper functions and classes to easily use database dumps.

## API Quick start
```
from vndb_thigh_highs import VNDB
from vndb_thigh_highs.models import VN

vndb = VNDB()
vns = vndb.get_vn(VN.id == 17)
vn = vns[0]
print(vn.title)
```

[Check the documentation for more details](https://code.blicky.net/FoieGras/vndb-thigh-highs/src/branch/master/docs/vndb_api.md)

## Dumps Quick start
```
from vndb_thigh_highs.dumps import TraitDatabaseBuilder

builder = TraitDatabaseBuilder()
trait_db = builder.build_with_archive("path/to/traits.json.gz")
trait_id = 186
trait = trait_db.get_trait(trait_id)
print(trait.name)
```

[Check the documentation for more details](https://code.blicky.net/FoieGras/vndb-thigh-highs/src/branch/master/docs/dump_helpers.md)

## Testing
Run `test/main.py`.

By default tests are run using predefined responses. It is possible to run them with vndb by editing `use_mock_socket = True` in `test/test_case.py`, though logged in tests require valid credentials in `data/login.json`. A few troublesome tests are also skipped when using vndb.

Database dumps tests will need dumps, compressed and decompressed, in `data/`.

## License
This module is licensed under the AGPLv3.
