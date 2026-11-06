# === Stage 3: Хранилище в памяти ===
# Project: SwimSplits
import uuid
from datetime import datetime


class SwimSplitsError(Exception):
    pass


class Lap:
    def __init__(self, style, distance, time, splits=None):
        self.id = uuid.uuid4().hex
        self.style = style
        self.distance = distance
        self.time = time
        self.splits = splits or []


class SwimSessionStore:
    def __init__(self):
        self._laps = {}

    def add_lap(self, lap):
        self._laps[lap.id] = lap
        return lap

    def get_lap(self, lap_id):
        lap = self._laps.get(lap_id)
        if lap is None:
            raise SwimSplitsError(f"Заплыв {lap_id} не найден")
        return lap

    def list_laps(self):
        return list(self._laps.values())


def validate_lap(lap):
    if not lap.style:
        raise SwimSplitsError("Стиль заплыва обязателен")
    if not lap.distance:
        raise SwimSplitsError("Дистанция заплыва обязательна")
    if not lap.time:
        raise SwimSplitsError("Время заплыва обязательно")
    return lap


def build_sample_store():
    store = SwimSessionStore()
    store.add_lap(Lap("кроль", 1.5, "1:30", ["0:45", "0:45"]))
    store.add_lap(Lap("спинк", 50.0, "5:00", ["1:30", "1:30", "1:30"]))
    return store


if __name__ == "__main__":
    store = build_sample_store()
    for lap in store.list_laps():
        print(f"{lap.style}: {lap.distance} м за {lap.time}")
    print(store.get_lap(store.list_laps()[0].id))
