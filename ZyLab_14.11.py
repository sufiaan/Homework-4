"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZYLAB-14.11
"""
def selection_sort_descend_trace(alist):

    for i in range(len(alist)-1):
        index = i
        for j in range(i + 1, len(alist)):
            if alist[index] < alist[j]:
                index = j
        alist[i], alist[index] = alist[index], alist[i]

        for x in alist:
            print(x, end=" ")
        print()
    return alist

if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
