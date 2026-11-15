# === Stage 7: Генерация идентификаторов ===
# Project: SwimSplits
import string
import uuid


PROJECT_PREFIX = "swim"


def _is_valid_identifier(identifier: str) -> bool:
    if not identifier or identifier.startswith("-"):
        return False
    if len(identifier) > 128:
        return False
    for char in identifier:
        if not (char.isalnum() or char in "_"):
            return False
    return True


def generate_unique_id(prefix: str = PROJECT_PREFIX, counter: dict = None) -> str:
    if counter is None:
        counter = {}
    while True:
        candidate = f"{prefix}-{uuid.uuid4().hex}"
        if counter.get(candidate) is None:
            counter[candidate] = True
            return candidate


def generate_sequential_id(prefix: str = PROJECT_PREFIX, counter: dict = None) -> str:
    if counter is None:
        counter = {}
    while True:
        candidate = f"{prefix}-{counter.get(prefix, 0):06d}"
        if candidate not in counter:
            counter[candidate] = True
            counter[prefix] = int(candidate.split("-")[-1]) + 1
            return candidate


def sanitize_identifier(identifier: str) -> str:
    cleaned = "".join(char for char in identifier if char.isalnum() or char == "_")
    if not cleaned:
        cleaned = "entity"
    return cleaned.lower()


def validate_unique_ids(known_ids: set, new_ids: list) -> list:
    collisions = []
    for identifier in new_ids:
        if identifier in known_ids:
            collisions.append(identifier)
    return collisions


def build_id_map(records: list, prefix: str = PROJECT_PREFIX) -> dict:
    id_map = {}
    for record in records:
        identifier = generate_unique_id(prefix, id_map)
        id_map[identifier] = record
    return id_map
