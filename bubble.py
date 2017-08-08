# coding:utf-8


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    a = [6, 4, 2, 1, 7, 5]
    print bubble_sort(a)