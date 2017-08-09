# coding:utf-8


def sort(lists):
    return quick_sort(lists, 0, len(lists) - 1)


def quick_sort(lists, left, right):
    if left > right:
        return lists
    key = lists[left]
    low = left
    high = right

    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]

        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]

    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


def quick_sort_copy(lists):
    if len(lists) <= 1:
        return lists
    key = lists[0]
    l1 = quick_sort_copy([i for i in lists if i < key])
    l2 = quick_sort_copy([i for i in lists if i >= key])
    return l1 + l2


def _quick_sort(L):
    if len(L) <= 1:
        return L
    return _quick_sort([lt for lt in L[1:] if lt < L[0]]) + [L[0]] + _quick_sort([ge for ge in L[1:] if ge >= L[0]])


if __name__ == '__main__':
    a = [6, 4, 2, 1, 7, 5]
    print sort(a)
