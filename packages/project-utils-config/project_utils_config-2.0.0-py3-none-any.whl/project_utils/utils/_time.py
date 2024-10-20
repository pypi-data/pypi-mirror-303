from typing import Optional

from datetime import datetime, timedelta


def datetime_to_str(dt: Optional[datetime] = None, format: str = "%Y-%m-%d %H:%M:%S") -> str:
    if dt is None:
        dt = datetime.now()
    return dt.strftime(format)


def datetime_to_timestamp(dt: Optional[datetime] = None) -> int:
    if dt is None:
        dt = datetime.now()
    return int(dt.timestamp() * 1000)


def str_to_datetime(time_str: str, format: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    return datetime.strptime(time_str, format)


def str_to_timestamp(time_str: str, format: str = "%Y-%m-%d %H:%M:%S") -> int:
    return datetime_to_timestamp(str_to_datetime(time_str, format))


def timestamp_to_datetime(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp)


def timestamp_to_str(timestamp: int, format: str = "%Y-%m-%d %H:%M:%S") -> str:
    return datetime_to_str(timestamp_to_datetime(timestamp), format=format)


def compute_by_year(year: int = 0, dt: Optional[datetime] = None) -> datetime:
    if dt is None:
        dt = datetime.now()
    year: int = dt.year - year
    month: int = dt.month
    day: int = dt.day
    return datetime(year, month, day)


def compute_by_month(month: int = 0, dt: Optional[datetime] = None) -> datetime:
    if dt is None:
        dt = datetime.now()
    year: int = dt.year
    month: int = dt.month - month
    day: int = dt.day
    return datetime(year, month, day)


def compute_by_week(week: int = 0, dt: Optional[datetime] = None) -> datetime:
    if dt is None:
        dt = datetime.now()
    return dt + timedelta(weeks=week)


def compute_by_day(day: int = 0, dt: Optional[datetime] = None) -> datetime:
    if dt is None:
        dt = datetime.now()
    return dt + timedelta(days=day)


def compute_by_hour(hour: int = 0, dt: Optional[datetime] = None) -> datetime:
    if dt is None:
        dt = datetime.now()
    return dt + timedelta(hours=hour)


def compute_by_minute(minute: int = 0, dt: Optional[datetime] = None) -> datetime:
    if dt is None:
        dt = datetime.now()
    return dt + timedelta(minutes=minute)


def compute_by_second(second: int = 0, dt: Optional[datetime] = None) -> datetime:
    if dt is None:
        dt = datetime.now()
    return dt + timedelta(seconds=second)


if __name__ == '__main__':
    ...
