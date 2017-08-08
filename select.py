# coding:utf-8


def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


if __name__ == '__main__':
    a = [6, 4, 2, 1, 7, 5]
    print select_sort(a)
