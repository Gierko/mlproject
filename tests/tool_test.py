from mlproject.tools import haversine

import pytest

out = haversine(2.380009, 48.865070, 2, 48)

assert out == 100.19353920046613
