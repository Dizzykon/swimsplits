# === Stage 9: Текстовый поиск ===
# Project: SwimSplits
def highlight_field(value, needle):
    if not needle:
        return value
    text = str(value)
    index = 0
    result = []
    needle_len = len(needle)
    while True:
        pos = text.find(needle, index)
        if pos == -1:
            result.append(text[index:])
            break
        result.append(text[index:pos])
        result.append(needle)
        index = pos + needle_len
    return "".join(result)


def build_query(texts, keywords):
    if not keywords:
        return texts
    combined = " ".join(keywords)
    lowered = combined.lower()
    lowered_texts = [t.lower() for t in texts]
    mask = [l in lowered for l, t in zip(lowered, lowered_texts)]
    return [t if m else "" for t, m in zip(texts, mask)]


def search_swims(swims, keyword):
    if not keyword:
        return list(swims)
    lowered = keyword.lower()
    found = []
    for swim in swims:
        fields = [swim.get("date", ""), swim.get("style", ""), swim.get("distance", "")]
        if any(lowered in str(f).lower() for f in fields):
            found.append(swim)
    return found


def highlight_match(text, keyword):
    if not keyword:
        return text
    lowered = keyword.lower()
    lowered_text = str(text).lower()
    index = 0
    result = []
    while True:
        pos = lowered_text.find(lowered, index)
        if pos == -1:
            result.append(str(text)[index:])
            break
        result.append(str(text)[index:pos])
        result.append(keyword)
        index = pos + len(keyword)
    return "".join(result)
