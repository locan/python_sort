# -*- coding:utf-8 -*-


def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group], lists[k] = lists[k], k
                    k -= group
                j += group
        group /= step
    return lists


if __name__ == '__main__':
    l = [8, 5, 3, 1, 7, 4, 2]
    print shell_sort(l)
