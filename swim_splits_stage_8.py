# === Stage 8: Фильтрация записей ===
# Project: SwimSplits
from datetime import date


def filter_swims(swims, style=None, start_date=None, end_date=None):
    result = []
    for swim in swims:
        if style is not None and swim.get("style") != style:
            continue
        if start_date is not None and swim.get("date") < start_date:
            continue
        if end_date is not None and swim.get("date") > end_date:
            continue
        result.append(swim)
    return result


def filter_by_style(swims, style):
    return [swim for swim in swims if swim.get("style") == style]


def filter_by_date_range(swims, start_date, end_date):
    return [
        swim
        for swim in swims
        if start_date <= swim.get("date") <= end_date
    ]


def filter_swims_by_style_and_date(
    swims, style=None, start_date=None, end_date=None
):
    if style is not None:
        swims = filter_by_style(swims, style)
    if start_date is not None or end_date is not None:
        swims = filter_by_date_range(swims, start_date, end_date)
    return swims


if __name__ == "__main__":
    demo = [
        {
            "date": date(2024, 1, 15),
            "style": "freestyle",
            "distance": 1500,
            "time": 1020,
        },
        {
            "date": date(2024, 2, 10),
            "style": "backstroke",
            "distance": 500,
            "time": 340,
        },
        {
            "date": date(2024, 3, 5),
            "style": "freestyle",
            "distance": 1000,
            "time": 760,
        },
    ]

    print("Все записи:")
    for swim in demo:
        print(swim)

    print("\nТолько freestyle:")
    for swim in filter_by_style(demo, "freestyle"):
        print(swim)

    print("\nЗаписи за 2024 год:")
    for swim in filter_by_date_range(demo, date(2024, 1, 1), date(2024, 12, 31)):
        print(swim)

    print("\nFreestyle за 2024 год:")
    for swim in filter_swims_by_style_and_date(
        demo, "freestyle", date(2024, 1, 1), date(2024, 12, 31)
    ):
        print(swim)
