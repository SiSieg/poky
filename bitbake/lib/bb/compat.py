"""Code pulled from future python versions, here for compatibility"""

import sys
if sys.version_info[:2] >= (3, 8):
    from collections.abc import MutableMapping, KeysView, ValuesView, ItemsView
else:
    from collections import MutableMapping, KeysView, ValuesView, ItemsView

from collections import OrderedDict
from functools import total_ordering


