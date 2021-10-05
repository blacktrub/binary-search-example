EMPTY_VALUE = -1


def recursive_binary_search(rows: list, target: int) -> int:
    if not rows:
        return EMPTY_VALUE

    middle = len(rows) // 2
    middle_val = rows[middle]
    if middle_val == target:
        return middle

    if middle_val > target:
        return recursive_binary_search(rows[:middle], target)
    else:
        return recursive_binary_search(rows[middle + 1:], target) + middle + 1


def loop_binary_search(rows: list, target: int) -> int:
    if not rows:
        return EMPTY_VALUE

    start, end = 0, len(rows)
    while True:
        middle = (end - start) // 2 + start
        middle_val = rows[middle]
        if middle_val == target:
            return middle

        if middle_val > target:
            end = middle
        else:
            start = middle + 1

        if not rows[start:end]:
            return EMPTY_VALUE
