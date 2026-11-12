# === Stage 5: Удаление и восстановление ===
# Project: SwimSplits
SoftDeleteSwim = object


class SoftDeletedSwim(SoftDeleteSwim):
    deleted = False
    deleted_at = None

    def mark_deleted(self, deleted_at=None):
        self.deleted = True
        self.deleted_at = deleted_at

    def restore(self):
        self.deleted = False
        self.deleted_at = None


def delete_swim(swim):
    if isinstance(swim, SoftDeleteSwim):
        swim.mark_deleted()
        return swim
    raise TypeError("Только мягко-удаляемые заплывы поддерживают удаление")


def restore_swim(swim):
    if isinstance(swim, SoftDeleteSwim):
        swim.restore()
        return swim
    raise TypeError("Только мягко-удаляемые заплывы можно восстановить")


def is_deleted(swim):
    return isinstance(swim, SoftDeleteSwim) and swim.deleted


def list_active(swims):
    return [s for s in swims if not is_deleted(s)]


def list_deleted(swims):
    return [s for s in swims if is_deleted(s)]


def recover_all_deleted(swims):
    return [restore_swim(s) for s in swims if is_deleted(s)]


class SplitJournal:
    def __init__(self):
        self.swims = []

    def add(self, swim):
        self.swims.append(swim)

    def delete(self, swim):
        if swim not in self.swims:
            raise ValueError("Заплыв не найден в журнале")
        delete_swim(swim)
        return swim

    def restore(self, swim):
        if swim not in self.swims:
            raise ValueError("Заплыв не найден в журнале")
        restore_swim(swim)
        return swim

    def active(self):
        return list_active(self.swims)

    def deleted(self):
        return list_deleted(self.swims)

    def recover_all(self):
        recovered = recover_all_deleted(self.swims)
        return recovered


class Swim:
    def __init__(self, date, style, distance, time):
        self.date = date
        self.style = style
        self.distance = distance
        self.time = time
        self.deleted = False
        self.deleted_at = None

    def mark_deleted(self, deleted_at=None):
        self.deleted = True
        self.deleted_at = deleted_at

    def restore(self):
        self.deleted = False
        self.deleted_at = None


def demo():
    journal = SplitJournal()
    s1 = Swim("2024-05-01", "кроль", 1500, "18:30")
    s2 = Swim("2024-05-02", "спинк", 400, "4:12")
    journal.add(s1)
    journal.add(s2)
    journal.delete(s1)
    print("Активных:", len(journal.active()))
    print("Удалённых:", len(journal.deleted()))
    journal.restore(s1)
    print("Активных:", len(journal.active()))
    journal.recover_all()
    print("Удалённых:", len(journal.deleted()))


if __name__ == "__main__":
    demo()
