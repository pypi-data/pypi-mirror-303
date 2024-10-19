"""Math utils"""

import math


# calculate bits of integer in base
def int_bits(num, base: int = 10):
    return math.ceil(math.log(num + 1, base))


# get max length of dict keys
def max_key_len(d: dict, offset: int = 0):
    if not d:
        return 0
    return max([len(str(k)) + offset for k in d.keys()])
