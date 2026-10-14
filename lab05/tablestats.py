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
