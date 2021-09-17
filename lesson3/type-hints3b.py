import json
from typing import cast

x = json.loads("[1,2,3]")

reveal_type(x)

y = cast(dict, x)

reveal_type(y)

reveal_locals()
