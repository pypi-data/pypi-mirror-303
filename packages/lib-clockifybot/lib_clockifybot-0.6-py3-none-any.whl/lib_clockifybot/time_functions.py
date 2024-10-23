from datetime import datetime as dt, timedelta as td

import pytz

tehran_tz = pytz.timezone('Asia/Tehran')


def duration_to_time(duration_str):
    duration_str = duration_str[2:]
    hours, minutes, seconds = 0, 0, 0
    start = 0
    for i, char in enumerate(duration_str):
        if not char.isdigit():
            end = i
            if char == "H":
                hours = int(duration_str[start:end])
            elif char == "M":
                minutes = int(duration_str[start:end])
            elif char == "S":
                seconds = int(duration_str[start:end])
            start = i + 1
    return td(hours=hours, minutes=minutes, seconds=seconds)


def daily_interval(selected_date):
    end_date = selected_date + td(days=1)
    start_date = selected_date
    e_year, e_month, e_day = end_date.year, end_date.month, end_date.day
    s_year, s_month, s_day = start_date.year, start_date.month, start_date.day
    end = dt(year=e_year, month=e_month, day=e_day, hour=0, minute=0, second=0)
    start = dt(year=s_year, month=s_month, day=s_day, hour=0, minute=0, second=0)
    return [start, end]


def normal2clockify(norm_date):
    return f"{norm_date.strftime('%Y-%m-%dT%H:%M:%SZ')}"


def to_iso_8601_duration(timedelta):
    seconds = int(timedelta.total_seconds())
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    zero = 0
    duration_str = "PT"
    if hours > zero:
        duration_str += f"{hours}H"
    if minutes > zero:
        duration_str += f"{minutes}M"
    if seconds > zero or (hours == zero and minutes == zero):
        duration_str += f"{seconds}S"
    return duration_str


def calculate_duration(time_str):
    user_start_time = dt.strptime(time_str, "%H:%M:%S")
    end_last_record = str(dt.now(tehran_tz))[11:19]
    user_end_time = dt.strptime(end_last_record, "%H:%M:%S")
    modified_start_time = user_start_time + td(hours=3, minutes=30)
    time_difference = user_end_time - modified_start_time
    duration = duration_to_time(to_iso_8601_duration(time_difference))
    return duration


def get_duration(record):
    if record["timeInterval"]["duration"]:
        return duration_to_time(record["timeInterval"]["duration"])
    else:
        return calculate_duration((record["timeInterval"]["start"])[11:19])
