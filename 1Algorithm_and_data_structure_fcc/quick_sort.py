"""使用quick sort对array进行排序"""


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # list comprehension
        # new list = [expression for member in iterable if condition]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 2, 3]))
