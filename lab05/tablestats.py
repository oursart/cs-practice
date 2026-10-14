def read_rows(lines):
    lst = []
    header = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = [s.strip() for s in line.split(',')]

        if header is None:
            header = parts
        elif len(parts) == len(header):
            lst.append(dict(zip(header, parts)))

    return lst


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows, kind):
    ans = 0.0
    for row in rows:
        if row["тип"] == kind:
            try:
                ans += float(row["минуты"].replace(",", "."))
            except ValueError:
                pass
    return round(ans, 1)
