import time
from datetime import datetime

from icecream import ic


def time_format():
    return f"{datetime.now()}|>"


def plus_five(num):
    return num + 5


def hello(user: bool):
    if user:
        ic(user)
    else:
        ic(user)


ic.configureOutput(prefix=time_format, includeContext=True)

ic(plus_five(4))
ic(plus_five(5))

hello(user=True)
hello(user=False)

for _ in range(3):
    time.sleep(1)
    ic("Hello")
