# === Stage 2: Проверка полей ===
# Project: SwimSplits
import datetime

VALID_STYLES = {"кроль", "спина", "брас", "баттерфляй", "смешанный"}
DATE_FORMAT = "%Y-%m-%d"


class SwimSessionValidationError(Exception):
    pass


def normalize_date(value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, str):
        for fmt in (DATE_FORMAT, "%d.%m.%Y", "%d/%m/%Y", "%m-%d-%Y"):
            try:
                return datetime.datetime.strptime(value.strip(), fmt).date()
            except ValueError:
                continue
        raise SwimSessionValidationError(
            "Дата должна быть в формате ГГГГ-ММ-ДД, например 2024-06-15"
        )
    raise SwimSessionValidationError("Дата должна быть строкой или датой")


def normalize_style(value):
    if isinstance(value, str):
        normalized = value.strip().lower().replace(" ", "_").replace("-", "_")
        if normalized in VALID_STYLES:
            return normalized
        raise SwimSessionValidationError(
            f"Неизвестный стиль заплыва. Допустимые значения: {', '.join(sorted(VALID_STYLES))}"
        )
    if isinstance(value, (int, float)):
        style_map = {1: "кроль", 2: "спина", 3: "брас", 4: "баттерфляй", 5: "смешанный"}
        if value in style_map:
            return style_map[value]
        raise SwimSessionValidationError("Стиль заплыва должен быть от 1 до 5")
    raise SwimSessionValidationError("Стиль заплыва должен быть строкой или числом")


def normalize_distance(value):
    try:
        distance = float(value)
    except (TypeError, ValueError):
        raise SwimSessionValidationError("Дистанция должна быть числом")
    if distance <= 0:
        raise SwimSessionValidationError("Дистанция должна быть больше нуля")
    if distance > 1500:
        raise SwimSessionValidationError("Дистанция не может превышать 1500 метров")
    return distance


def normalize_time(seconds):
    try:
        seconds = float(seconds)
    except (TypeError, ValueError):
        raise SwimSessionValidationError("Время должно быть числом в секундах")
    if seconds <= 0:
        raise SwimSessionValidationError("Время должно быть больше нуля")
    return seconds


def normalize_session(session_data):
    if not isinstance(session_data, dict):
        raise SwimSessionValidationError("Запись заплыва должна быть словарём")
    date = normalize_date(session_data.get("date"))
    style = normalize_style(session_data.get("style"))
    distance = normalize_distance(session_data.get("distance"))
    time = normalize_time(session_data.get("time"))
    return {
        "date": date,
        "style": style,
        "distance": distance,
        "time": time,
    }
