def _sub_search(arr, s, lower, upper):
    center = (lower + upper) / 2
    explore_lower = True

    next_lower = center
    next_higher = center + 1

    while True:
        if explore_lower:
            i = next_lower
            next_lower -= 1
        else:
            i = next_higher
            next_higher += 1
        explore_lower = not explore_lower
        if i < lower or i > upper:
            break
        if arr[i] != "":
            return (i, cmp(s, arr[i]))

    return None


def search(arr, s):
    assert type(arr) is list
    assert type(s) is str
    if len(arr) == 0:
        return -1   # not found

    lower = 0
    upper = len(arr) - 1

    while True:
        retval = _sub_search(arr, s, lower, upper)

        if retval is None:
            return -1   # not found
        i, cmp_result = retval
        if cmp_result == 0:
            return i    # found!
        if cmp_result < 0:
            # look for s in the region lower than i
            upper = i - 1
            if upper < lower:
                return -1   # not found
        else:
            lower = i + 1
            if lower > upper:
                return -1   # not found
