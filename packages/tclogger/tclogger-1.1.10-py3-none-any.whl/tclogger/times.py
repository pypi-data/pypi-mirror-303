"""Time utils"""

from datetime import datetime, timedelta
from typing import Literal

from .colors import colored
from .logs import logger, add_fillers


def get_now() -> datetime:
    return datetime.now()


def get_now_ts() -> int:
    return int(datetime.now().timestamp())


def get_now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def ts_to_str(ts: int) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def str_to_ts(s: str) -> int:
    return int(datetime.fromisoformat(s).timestamp())


def t_to_str(t: datetime) -> str:
    return t.strftime("%Y-%m-%d %H:%M:%S")


def t_to_ts(t: datetime) -> int:
    return int(t.timestamp())


def dt_to_sec(dt: timedelta, precision: int = 0) -> float:
    if precision is not None and precision > 0:
        return round(dt.total_seconds(), ndigits=precision)
    else:
        return int(dt.total_seconds())


def dt_to_str(
    dt: timedelta,
    precision: int = 0,
    str_format: Literal["unit", "colon"] = "colon",
) -> str:
    hours = dt.days * 24 + dt.seconds // 3600
    minutes = (dt.seconds // 60) % 60
    seconds = dt.seconds % 60
    microseconds = dt.microseconds / 1000000
    precised_seconds = seconds + microseconds

    if str_format == "unit":
        hours_str = f"{hours}hr" if hours > 0 else ""
        minutes_str = f"{minutes}min" if minutes > 0 else ""
        if precision is not None and precision > 0:
            seconds_str = f"{precised_seconds:.{precision}f}s"
        else:
            seconds_str = f"{seconds}s"

        time_str = " ".join([hours_str, minutes_str, seconds_str]).strip()
    else:
        hours_str = f"{hours:02d}" if hours > 0 else ""
        minutes_str = f"{minutes:02d}"
        seconds_str = f"{seconds:02d}"
        time_str = ":".join([hours_str, minutes_str, seconds_str]).strip(":")

    return time_str


def get_now_ts_str() -> tuple[int, str]:
    now = datetime.now()
    now_ts = int(now.timestamp())
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return now_ts, now_str


class Runtimer:
    def __init__(self, verbose=True):
        self.verbose = verbose

    def __enter__(self):
        self.start_time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time()
        self.elapsed_time()

    def start_time(self):
        self.t1 = datetime.now()
        self.logger_time("start", self.t1)
        return self.t1

    def end_time(self):
        self.t2 = datetime.now()
        self.logger_time("end", self.t2)
        return self.t2

    def elapsed_time(self):
        self.dt = self.t2 - self.t1
        self.logger_time("elapsed", self.dt)
        return self.dt

    def logger_time(self, time_type, t):
        time_types = {
            "start": "Start",
            "end": "End",
            "elapsed": "Elapsed",
        }
        if self.verbose:
            time_str = add_fillers(
                colored(
                    f"{time_types[time_type]} time: [ {self.time2str(t)} ]",
                    "light_magenta",
                ),
                fill_side="both",
            )
            logger.line(time_str)

    # Convert time to string
    def time2str(self, t, unit_sep=" "):
        if isinstance(t, datetime):
            datetime_str_format = "%Y-%m-%d %H:%M:%S"
            return t.strftime(datetime_str_format)
        elif isinstance(t, timedelta):
            hours = t.seconds // 3600
            hour_str = f"{hours}{unit_sep}hr" if hours > 0 else ""
            minutes = (t.seconds // 60) % 60
            minute_str = f"{minutes:>2}{unit_sep}min" if minutes > 0 else ""
            seconds = t.seconds % 60
            milliseconds = t.microseconds // 1000
            precised_seconds = seconds + milliseconds / 1000
            second_str = (
                f"{precised_seconds:>.1f}{unit_sep}s" if precised_seconds >= 0 else ""
            )
            time_str = " ".join([hour_str, minute_str, second_str]).strip()
            return time_str
        else:
            return str(t)
