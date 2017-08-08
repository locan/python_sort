# -*- coding:utf-8 -*-


def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i];
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1], lists[j] = lists[j], key

            j -= 1
    return lists


if __name__ == '__main__':
    a = [6, 4, 2, 1, 7, 5]
    print insert_sort(a)
