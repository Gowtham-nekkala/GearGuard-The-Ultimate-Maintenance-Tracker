from datetime import datetime

def parse_date(date_str):
    """
    Parses a date string in YYYY-MM-DD format.
    Returns date object or None.
    """
    try:
        if date_str:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        pass
    return None

def format_duration(hours):
    """
    Formats duration hours into a readable string.
    e.g. 2.5 -> "2h 30m"
    """
    h = int(hours)
    m = int((hours - h) * 60)
    return f"{h}h {m}m"
