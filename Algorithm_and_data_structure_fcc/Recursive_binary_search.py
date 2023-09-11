def binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return binary_search(list[midpoint + 1 :], target)
            else:
                return binary_search(list[: midpoint - 1], target)


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

verify(binary_search(Numbers, 6))
verify(binary_search(Numbers, 12))
