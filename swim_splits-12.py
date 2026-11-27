# === Stage 12: Слияние записей ===
# Project: SwimSplits
from datetime import date


def merge_swims(a, b, field):
    if field == "date":
        return a if a >= b else b
    if field == "style":
        return a if a in ("freestyle", "backstroke", "breaststroke", "butterfly", "individual_mixed") else b
    if field == "distance":
        return a if a > b else b
    if field == "time":
        return a if a < b else b
    return b


def merge_record(swim, field):
    if field == "date":
        return swim.date
    if field == "style":
        return swim.style
    if field == "distance":
        return swim.distance
    if field == "time":
        return swim.time
    return None


def combine_swims(swim1, swim2, fields):
    result = dict(swim1)
    for field in fields:
        result[field] = merge_swims(swim1, swim2, field)
    return result


def update_record(record, swim, fields):
    for field in fields:
        record[field] = merge_record(swim, field)
    return record


def best_time(times):
    return min(times)


def best_distance(distances):
    return max(distances)


def best_date(dates):
    return max(dates)


def best_style(styles):
    return max(styles, key=styles.count)


def personal_records(records):
    pr = {}
    for record in records:
        for field in record:
            if field in pr:
                pr[field] = merge_record(record, field)
            else:
                pr[field] = merge_record(record, field)
    return pr


def merge_singles(record, swim1, swim2):
    merged = merge_swims(swim1, swim2, "time")
    return merge_record(record, "time")
