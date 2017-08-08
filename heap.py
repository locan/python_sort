# coding:utf-8


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists


def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        adjust_heap(lists, i, size)


def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[i], lists[max] = lists[max], lists[i]
            adjust_heap(lists, max, size)


if __name__ == '__main__':
    a = [6, 4, 2, 1, 7, 5]
    print heap_sort(a)
