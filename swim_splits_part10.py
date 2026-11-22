# === Stage 10: Постраничный вывод ===
# Project: SwimSplits
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple


@dataclass
class SwimSession:
    date: str
    style: str
    distance: float
    total_time: float
    splits: List["Split"] = field(default_factory=list)


@dataclass
class Split:
    distance: float
    time: float


@dataclass
class PageMetadata:
    page: int
    page_size: int


def clamp(value: int, lower: int, upper: int) -> int:
    return max(lower, min(value, upper))


def paginate(sessions: Sequence[SwimSession], page: int, page_size: int) -> Tuple[List[SwimSession], PageMetadata]:
    if page_size <= 0:
        raise ValueError("page_size must be positive")
    if page < 1:
        raise ValueError("page must be >= 1")

    total = len(sessions)
    total_pages = (total + page_size - 1) // page_size if total else 0
    if total_pages == 0:
        return [], PageMetadata(page=1, page_size=page_size)

    page = clamp(page, 1, total_pages)
    start = (page - 1) * page_size
    end = start + page_size
    return list(sessions[start:end]), PageMetadata(page=page, page_size=page_size)


def split_summary(sessions: Sequence[SwimSession]) -> List[Tuple[str, float, float]]:
    result = []
    for session in sessions:
        best = min(session.splits, key=lambda s: s.time) if session.splits else None
        if best:
            result.append((session.style, best.distance, best.time))
    return result
