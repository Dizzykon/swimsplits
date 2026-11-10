# === Stage 4: Редактирование записей ===
# Project: SwimSplits
from datetime import date

ALLOWED_SWIM_FIELDS = ("style", "distance", "time")


def can_update_swim(swim, changes):
    changed_fields = set(changes)
    return changed_fields.issubset(set(ALLOWED_SWIM_FIELDS))


def validate_changes(swim, changes):
    new_style = changes.get("style")
    new_distance = changes.get("distance")
    new_time = changes.get("time")

    if new_style is not None:
        if new_style not in ("freestyle", "backstroke", "breaststroke", "butterfly", "individual_mixed"):
            raise ValueError("Недопустимое значение стиля: {}".format(new_style))

    if new_distance is not None:
        if not isinstance(new_distance, (int, float)) or new_distance <= 0:
            raise ValueError("Дистанция должна быть положительным числом")

    if new_time is not None:
        if not isinstance(new_time, (int, float)) or new_time <= 0:
            raise ValueError("Время должно быть положительным числом")


def update_swim(swim, changes, swim_id):
    if swim_id != swim["id"]:
        raise KeyError("Заплыв с идентификатором {} не найден".format(swim_id))

    if not can_update_swim(swim, changes):
        raise ValueError("Допустимо менять только поля: {}".format(ALLOWED_SWIM_FIELDS))

    validate_changes(swim, changes)

    for field, value in changes.items():
        swim[field] = value

    return swim
