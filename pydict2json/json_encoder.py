import json
import math
from decimal import Decimal


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            if obj.is_nan():
                return math.nan
            return str(obj)
        return super().default(obj)
