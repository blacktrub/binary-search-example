EMPTY_VALUE = -1


def binary_search(rows: list, target: int) -> int:
    if not rows:
        return EMPTY_VALUE

    middle = len(rows) // 2
    middle_val = rows[middle]
    if middle_val == target:
        return middle

    if middle_val > target:
        return binary_search(rows[:middle], target)
    else:
        return binary_search(rows[middle + 1:], target) + middle + 1
