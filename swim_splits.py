# === Stage 1: Каркас модуля ===
# Project: SwimSplits
from datetime import date
from typing import List


SWIM_STYLES = ("кроль", "спинк", "брас", "баттерфляй")
DISTANCE_UNITS = ("м", "км")


@dataclass
class SwimSession:
    date: date
    style: str
    distance: float
    time: float


@dataclass
class Split:
    distance: float
    time: float


def create_demo_sessions() -> List[SwimSession]:
    return [
        SwimSession(date(2024, 1, 15), "кроль", 1.5, 150.5),
        SwimSession(date(2024, 1, 16), "баттерфляй", 0.5, 70.2),
        SwimSession(date(2024, 1, 17), "спинк", 1.0, 110.0),
    ]


def main() -> None:
    print("SwimSplits — журнал заплывов")
    print("Стили:", ", ".join(SWIM_STYLES))
    print("Дистанции:", ", ".join(DISTANCE_UNITS))
    for session in create_demo_sessions():
        print(f"  {session.date} | {session.style} | "
              f"{session.distance} {session_distance(session.distance)} | "
              f"{session_time(session.time)}")


if __name__ == "__main__":
    main()
