import platform
import sys
import uuid
from datetime import datetime

import arrow
import pytz
from babel.dates import format_datetime
from cowsay.__main__ import cli


def os():
    print(platform.system())


def say():
    cli()


def ts():
    timestamp = arrow.now().timestamp()
    print(int(timestamp))


def ms():
    timestamp = arrow.now().timestamp()
    print(int(timestamp * 1000))


def gen_uuid():
    print(uuid.uuid4())


def py_version():
    print(f"🧊 python:{sys.version}")


def strf_time(zone: str):
    tz = pytz.timezone(zone)
    now = datetime.now(tz)
    # locale="zh_CN" 会使月份和星期的名称显示为中文
    # locale="en_US" 则会显示为英文
    return format_datetime(
        now, "yyyy年MM月dd日 HH:mm:ss EEEE ZZZZ zzzz", locale="zh_CN"
    )


def print_strf_time():
    t0 = strf_time("UTC")
    t1 = strf_time("America/New_York")
    t2 = strf_time("Asia/Shanghai")

    print(t0)
    print(t1)
    print(t2)
