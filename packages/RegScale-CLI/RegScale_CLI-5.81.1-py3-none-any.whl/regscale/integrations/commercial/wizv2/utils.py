import datetime

from regscale.core.utils.date import datetime_obj


def convert_first_seen_to_days(first_seen: str) -> int:
    """
    Converts the first seen date to days
    :param str first_seen: First seen date
    :returns: Days
    :rtype: int
    """
    first_seen_date = datetime_obj(first_seen)
    if not first_seen_date:
        return 0
    first_seen_date_naive = first_seen_date.replace(tzinfo=None)
    return (datetime.datetime.now() - first_seen_date_naive).days
