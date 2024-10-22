from datetime import datetime
from typing import Optional


def get_formatted_date(date: Optional[datetime] = None) -> str:
    return (date or datetime.now()).isoformat(timespec="seconds").replace(":", "\uA789")
