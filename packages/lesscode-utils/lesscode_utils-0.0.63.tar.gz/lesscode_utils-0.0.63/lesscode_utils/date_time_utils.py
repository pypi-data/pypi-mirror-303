import importlib
import math
from datetime import datetime, timedelta, date
from typing import Union

from lesscode_utils.common_utils import fill


def date_time_add(date_time: Union[date, datetime], seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0,
                  months: int = 0, years: int = 0, is_format=False, template="%Y-%m-%d %H:%M:%S"):
    """
        时间偏移，可以正向偏移或者负向偏移，值大于0为正向偏移，值小于0为负向偏移
    :param date_time: 时间格式的时间
    :param seconds: 秒数
    :param minutes: 分钟数
    :param hours: 小时数
    :param days: 天数
    :param months: 月数
    :param years: 年数
    :param is_format: 是否格式化时间
    :param template: 格式时间模版
    :return:
    """
    if not any([isinstance(date_time, datetime), isinstance(date_time, date)]):
        raise Exception(f"date_time type = {type(date_time)} is error")
    date_time = date_time if isinstance(date_time, datetime) else datetime(year=date_time.year, month=date_time.month,
                                                                           day=date_time.day)
    date_time = date_time + timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
    final_year = date_time.year
    final_month = date_time.month
    if months:
        _final_month = date_time.month + months % 12
        _final_year = date_time.year + years + months // 12
        if _final_month > 12:
            final_month = _final_month % 12
            final_year += _final_month // 12
        elif _final_month < 0:
            final_month = _final_month % 12
            final_year -= _final_month // 12
        else:
            final_year = _final_year
            final_month = _final_month
    date_time = datetime(year=final_year, month=final_month, day=date_time.day,
                         hour=date_time.hour,
                         minute=date_time.minute, second=date_time.second)
    if is_format:
        date_str = date_time.strftime(template)
        return date_str
    else:
        return date_time


def date_time_diff(date_time1: datetime, date_time2: datetime, return_type: str = None,
                   digits: int = None):
    """
        时间差计算
    :param date_time1: 时间格式的时间
    :param date_time2: 时间格式的时间
    :param return_type: 不同单位的时间差的单位
    :param digits: 保留几位小数
    :return:
    """
    if date_time1 > date_time2:
        date_time1, date_time2 = date_time2, date_time1
    if return_type == "seconds":
        diff = date_time2 - date_time1
        return round(diff.total_seconds(), digits)
    elif return_type == "minutes":
        diff = date_time2 - date_time1
        return round(diff.total_seconds() / 60.0, digits)
    elif return_type == "hours":
        diff = date_time2 - date_time1
        return round(diff.total_seconds() / 3600.0, digits)
    elif return_type == "days":
        diff = date_time2 - date_time1
        return round(diff.total_seconds() / (3600.0 * 24), digits)
    elif return_type == "weeks":
        diff = date_time2 - date_time1
        return round(diff.total_seconds() / (3600.0 * 24 * 7), digits)
    elif return_type == "months":
        return round((date_time2.year - date_time1.year) * 12 + (date_time2.month - date_time1.month), digits)
    elif return_type == "years":
        return round(((date_time2.year - date_time1.year) + (date_time2.month - date_time1.month)) / 12.0,
                     digits)
    else:
        diff = date_time2 - date_time1
        return diff


def get_time_year(time: Union[date, datetime]):
    """
    获取时间的年份
    :param time:
    :return:
    """
    return time.year


def get_time_month(time: Union[date, datetime]):
    """
    获取时间的月份
    :param time:
    :return:
    """
    month_str = fill(time.month, 2, '0', position="font")
    return {"year": time.year, "month": time.month, "month_str": month_str, "full_month": f"{time.year}-{month_str}"}


def get_time_days(time: Union[date, datetime]):
    """
    获取时间的在一年中的第几天
    :param time:
    :return:
    """
    start_date = date(time.year - 1, 12, 31)
    end_date = time.date() if isinstance(time, datetime) else time
    return (end_date - start_date).days


def get_time_week(time: Union[date, datetime]):
    """
    获取时间在一年中的第几周
    :param time:
    :return:
    """
    week = math.ceil(get_time_days(time) / 7)
    return {"year": time.year, "month": time.month, "day": time.day, "days": get_time_days(time),
            "week": week, "full_week": f'{time.year}-{week}'}


def get_month_first_day(time: Union[date, datetime]):
    """
    获取时间当月的第一天
    :param time:
    :return:
    """
    first_day = date(time.year, time.month, 1)
    week_obj = get_time_week(first_day)
    return {"year": time.year, "month": time.month,
            "date": first_day,
            "week": week_obj.get("week"),
            "full_week": week_obj.get("full_week"),
            "date_str": f"{time.year}-{fill(time.month, 2, '0', position='font')}-{fill(first_day.day, 2, '0', position='font')}"}


def get_date(time: Union[date, datetime]):
    return time.date()


def get_week_first_day(time: Union[date, datetime]):
    week_start_day = time - timedelta(days=time.weekday())
    return week_start_day


def get_week_last_day(time: Union[date, datetime]):
    week_end_day = time + timedelta(days=6 - time.weekday())
    return week_end_day


def get_quarter_first_day(time: Union[date, datetime]):
    quarter_start_day = date(time.year, time.month - (time.month - 1) % 3, 1)
    return quarter_start_day


def get_quarter_last_day(time: Union[date, datetime]):
    try:
        relativedelta = importlib.import_module("dateutil.relativedelta")
    except ImportError:
        raise Exception(f"python-dateutil is not exist,run:pip install python-dateutil")
    quarter_end_day = (date(time.year, time.month - (time.month - 1) % 3 + 2, 1) +
                       relativedelta.relativedelta(months=1, days=-1))
    return quarter_end_day


def get_year_first_day(time: Union[date, datetime]):
    year_start_day = date(time.year, 1, 1)
    return year_start_day


def get_year_last_day(time: Union[date, datetime]):
    year_last_day = date(time.year, 12, 31)
    return year_last_day


def check_leap_year(year: int):
    """
    检查年份是平年还是闰年
    :param year:
    :return:
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def get_month_last_day(time: Union[date, datetime]):
    """
    获取当月的最后一天
    :param time:
    :return:
    """
    year = time.year
    month = time.month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = 31
    elif month == 2:
        if check_leap_year(year):
            day = 29
        else:
            day = 28
    else:
        day = 30
    last_day = date(time.year, time.month, day)
    week_obj = get_time_week(last_day)
    return {"year": time.year, "month": time.month,
            "day": day,
            "date": last_day,
            "week": week_obj.get("week"),
            "full_week": week_obj.get("full_week"),
            "date_str": f"{time.year}-{fill(time.month, 2, '0', position='font')}-{fill(last_day.day, 2, '0', position='font')}"}


def get_time_quarter(time: Union[date, datetime]):
    """
    获取时间所在的季度
    :param time:
    :return:
    """
    month = time.month
    quarter = math.ceil(month / 3)
    return {"year": time.year, "month": month, "quarter": quarter, "quarter_str": f"Q{quarter}",
            "full_quarter": f"{time.year}-Q{quarter}"}


def gen_date_series(start_time: Union[date, datetime], end_time: Union[date, datetime], series_type: str = "year"):
    """
    生成时间序列
    :param start_time:
    :param end_time:
    :param series_type:
    :return:
    """
    if series_type == "year":
        return [str(_) for _ in range(start_time.year, end_time.year + 1)]
    elif series_type == "month":
        months = []
        start_month_dict = get_time_month(start_time)
        start_year = start_month_dict.get("year")
        start_month = start_month_dict.get("month")
        end_month_dict = get_time_month(end_time)
        end_year = end_month_dict.get("year")
        end_month = end_month_dict.get("month")
        for year in range(start_year, end_year + 1):
            if year == start_year and start_year != end_year:
                for month in range(start_month, 12 + 1):
                    month_str = fill(month, 2, '0', position="font")
                    months.append(f"{year}-{month_str}")
            elif year == end_year and start_year != end_year:
                for month in range(1, end_month + 1):
                    month_str = fill(month, 2, '0', position="font")
                    months.append(f"{year}-{month_str}")
            elif year == end_year == start_year:
                for month in range(start_month, end_month + 1):
                    month_str = fill(month, 2, '0', position="font")
                    months.append(f"{year}-{month_str}")
            else:
                for month in range(1, 13):
                    month_str = fill(month, 2, '0', position="font")
                    months.append(f"{year}-{month_str}")
        return months
    elif series_type == "week":
        weeks = []
        start_week_dict = get_time_week(start_time)
        end_week_dict = get_time_week(end_time)
        start_year = start_week_dict.get("year")
        end_year = end_week_dict.get("year")
        start_week = start_week_dict.get("week")
        end_week = end_week_dict.get("week")
        for year in range(start_year, end_year + 1):
            if year == start_year and start_year != end_year:
                for week in range(start_week, 54):
                    weeks.append(f"{year}-{week}")
            elif year == end_year and start_year != end_year:
                for week in range(1, end_week + 1):
                    weeks.append(f"{year}-{week}")
            elif year == end_year == start_year:
                for week in range(start_week, end_week + 1):
                    weeks.append(f"{year}-{week}")
            else:
                for week in range(1, 54):
                    weeks.append(f"{year}-{week}")
        return weeks
    elif series_type == "quarter":
        quarters = []
        start_year = start_time.year
        start_month = start_time.month
        start_quarter = math.ceil(start_month / 3)
        end_year = end_time.year
        end_month = end_time.month
        end_quarter = math.ceil(end_month / 3)
        for year in range(start_year, end_year + 1):
            if year == start_year and start_year != end_year:
                for quarter in range(start_quarter, 5):
                    quarters.append(f"{year}-Q{quarter}")
            elif year == end_year and start_year != end_year:
                for quarter in range(1, end_quarter + 1):
                    quarters.append(f"{year}-Q{quarter}")
            elif year == end_year == start_year:
                for quarter in range(start_quarter, end_quarter + 1):
                    quarters.append(f"{year}-Q{quarter}")
            else:
                for quarter in range(1, 5):
                    quarters.append(f"{year}-Q{quarter}")
        return quarters
    elif series_type == "day":
        days = []
        start_month_dict = get_time_month(start_time)
        start_year = start_month_dict.get("year")
        start_month = start_month_dict.get("month")
        start_day = start_time.day
        end_month_dict = get_time_month(end_time)
        end_year = end_month_dict.get("year")
        end_month = end_month_dict.get("month")
        end_day = end_time.day
        for year in range(start_year, end_year + 1):
            if year == start_year and start_year != end_year:
                for month in range(start_month, 12 + 1):
                    last_day = get_month_last_day(start_time).get("day")
                    for day in range(start_day, last_day + 1):
                        days.append(
                            f"{year}-{fill(month, 2, '0', position='font')}-{fill(day, 2, '0', position='font')}")
            elif year == end_year and start_year != end_year:
                for month in range(1, end_month + 1):
                    for day in range(start_day, end_day + 1):
                        days.append(
                            f"{year}-{fill(month, 2, '0', position='font')}-{fill(day, 2, '0', position='font')}")
            elif year == end_year == start_year:
                if start_month == end_month:
                    for day in range(start_day, end_day + 1):
                        days.append(
                            f"{year}-{fill(start_month, 2, '0', position='font')}-{fill(day, 2, '0', position='font')}")
                else:
                    for month in range(start_month, end_month + 1):
                        _start_day = start_day if month == start_month else 1
                        _end_day = end_day if month == end_month else get_month_last_day(
                            date(year=year, month=month, day=1)).get("day")
                        for day in range(_start_day, _end_day + 1):
                            days.append(
                                f"{year}-{fill(month, 2, '0', position='font')}-{fill(day, 2, '0', position='font')}")
            else:
                for month in range(1, 13):
                    last_day = get_month_last_day(date(year=year, month=month, day=1)).get("day")
                    for day in range(1, last_day + 1):
                        days.append(
                            f"{year}-{fill(month, 2, '0', position='font')}-{fill(day, 2, '0', position='font')}")
        return days
    else:
        raise Exception(f"series_type={series_type} is not supported")


def get_date_time(date_str: str, template: str = "%Y-%m-%d %H:%M:%S", func: callable = None):
    """
    :param date_str: 时间字符串
    :param template: %Y:四位数的年份表示,%m:月份,%d:月内中的一天,%H:24小时制小时数,%M:分钟数,%S:秒,%A:本地完整星期名称,%Q:季度
    :param func: get_time_year，get_time_month，get_time_days，
                 get_time_week，get_month_last_day，get_month_first_day，
                 get_time_quarter,get_date，get_week_first_day，get_week_last_day，
                 get_quarter_first_day，get_quarter_last_day，get_year_first_day，get_year_last_day
    :return: 
    """
    date_time = datetime.strptime(date_str, template)
    if func:
        date_time = func(date_time)
    return date_time
