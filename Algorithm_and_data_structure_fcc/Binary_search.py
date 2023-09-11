def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

verify(binary_search(Numbers, 6))
verify(binary_search(Numbers, 12))
