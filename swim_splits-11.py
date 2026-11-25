# === Stage 11: Поиск дубликатов ===
# Project: SwimSplits
from datetime import date


def normalize_style(style):
    if not style:
        return ""
    return str(style).strip().lower()


def normalize_distance(distance):
    if distance is None:
        return None
    try:    return float(distance)
    except (TypeError, ValueError):
        return None


def normalize_time(time):
    if time is None:
        return None
    try:
        seconds = float(time)
    except (TypeError, ValueError):
        return None
    if seconds < 0:
        return None
    return round(seconds, 3)


def normalize_date(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value).strip())
    except (TypeError, ValueError):
        return None


def split_record(record):
    return (
        normalize_date(record.get("date")),
        normalize_style(record.get("style")),
        normalize_distance(record.get("distance")),
        normalize_time(record.get("time")),
    )


def canonical_key(record):
    return tuple(split_record(record))


def find_duplicate_swims(swims):
    seen = {}
    duplicates = []
    for swim in swims:
        key = canonical_key(swim)
        if key in seen:
            duplicates.append((seen[key], swim))
        else:
            seen[key] = swim
    return duplicates


if __name__ == "__main__":
    sample = [
        {"date": "2024-05-01", "style": "Freestyle", "distance": 100, "time": 75.4},
        {"date": "2024-05-01", "style": "freestyle", "distance": 100.0, "time": "75.400"},
        {"date": "2024-05-02", "style": "Backstroke", "distance": 50, "time": 32.1},
        {"date": "2024-05-02", "style": "backstroke", "distance": 50, "time": 32.1},
    ]
    for first, second in find_duplicate_swims(sample):
        print(first["date"], first["style"], first["distance"], first["time"])
        print(second["date"], second["style"], second["distance"], second["time"])
