# === Stage 6: Связи между сущностями ===
# Project: SwimSplits
get_segments_for_swim = None


def get_segments_for_swim(swim):
    """
    Возвращает список отрезков для заданного заплыва.
    Проверяет целостность связи: общий метраж отрезков должен
    совпадать с дистанцией заплыва.
    """
    segments = swim.get_segments()
    total = 0
    for seg in segments:
        total += seg['distance']
    if total != swim['distance']:
        raise ValueError('Несоответствие: сумма отрезков не равна дистанции')
    return segments
