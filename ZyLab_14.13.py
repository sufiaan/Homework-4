"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZYLAB-14.13
"""
# Global variable
num_calls = 0


def partition(user_ids, i, k):
    # TODO: Write the quicksort algorithm that recursively sorts the low and
    #       high partitions. Add 1 to num_calls each time quicksort() is called
    #  Pick middle element as pivot

    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]

    #  Initialize variables
    done = False
    l = i
    h = k

    while not done:
        #  incrementing l while user_ids[l] < pivot
        while user_ids[l] < pivot:
            l = l + 1
        #  Decrementing h while pivot < user_ids[h]

        while pivot < user_ids[h]:
            h = h - 1
        # If there are zero or one items remaining, all user_ids are partitioned. Return h

        if l >= h:
            done = True
        else:
            #  Swap user_ids[l] and user_ids[h], update l and h
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l = l + 1
            h = h - 1
    return h


def quicksort(user_ids, i, k):
    j = 0

    global num_calls
    num_calls = num_calls + 1

    if i >= k:
        return

    # Partition the data within the array. Value j returned from partitioning is location of last item in low partition
    j = partition(user_ids, i, k)

    # Recursively sort low partition (i to j) and high partition (j + 1 to k)

    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)