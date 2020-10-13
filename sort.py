
import random
import time
from recursioncounter import RecursionCounter
from sys import setrecursionlimit


#implement quicksort, return the sorted list
def quicksort(lyst):
    if isinstance(lyst, list):
        return quicksort_helper(0, len(lyst) - 1, lyst)
    else:
        raise ValueError("Parameter must be a list!")


def quicksort_helper(low, high, lyst):
    RecursionCounter() 
    if low < high:
        pivot_location = partition(low, high, lyst)
        quicksort_helper(low, pivot_location - 1, lyst)
        quicksort_helper(pivot_location + 1, high, lyst)


def partition(low, high, lyst):
    mid = (low + high) // 2
    pivot = lyst[mid]
    lyst[mid] = lyst[high]
    lyst[high] = pivot
    boundary = low
    for index in range(low, high):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    swap(lyst, high, boundary)
    return(boundary)


def swap(lyst, x, y):
    temp = lyst[x]
    lyst[x] = lyst[y]
    lyst[y] = temp


#implement mergesort, return the sorted list
def mergesort(lyst):
    if isinstance(lyst, list):
        buffer = list(lyst)
        return mergesort_helper(lyst, buffer, 0, len(lyst) - 1)
    else:
        raise ValueError("Parameter must be a list!")


def mergesort_helper(lyst, buffer, low, high):
    RecursionCounter()
    if low < high:
        mid = (low + high) // 2
        mergesort_helper(lyst, buffer, low, mid)
        mergesort_helper(lyst, buffer, mid + 1, high)
        merge(lyst, buffer, low, mid, high)


def merge(lyst, buffer, low, mid, high):
    item_1 = low
    item_2 = mid + 1
    for i in range(low, high + 1):
        if item_1 > mid:
            buffer[i] = lyst[item_2]
            item_2 += 1
        elif item_2 > high:
            buffer[i] = lyst[item_1]
            item_1 += 1
        elif lyst[item_1] < lyst[item_2]:
            buffer[i] = lyst[item_1]
            item_1 += 1
        else:
            buffer[i] = lyst[item_2]
            item_2 += 1
    for i in range(low, high + 1):
        lyst[i] = buffer[i]

#implement selection sort, return the sorted list
def selection_sort(lyst):
    if isinstance(lyst, list):
        for i in range(len(lyst)):
            min_index = i
            for j in range(i + 1, len(lyst)):
                if lyst[min_index] > lyst[j]:
                    min_index = j
            lyst[i], lyst[min_index] = lyst[min_index], lyst[i]
    else:
        raise ValueError("Parameter must be a list!")



#implement insertion sort, return the sorted list
def insertion_sort(lyst):
    if isinstance(lyst, list):
        for x in range(1, len(lyst)):
            y = x - 1
            while y >= 0 and lyst[x] < lyst[y]:
                lyst[y + 1] = lyst[y]
                y -= 1
            lyst[y + 1] = lyst[x]
    else:
        raise ValueError("Parameter must be a list!")



'''predicate function returns True if lyst is sorted, False otherwise. In
addition to verifying that lyst is a list, this should also verify that every element is an
integer'''
def is_sorted(lyst):
    if isinstance(lyst, list) and all(isinstance(x, int) for x in lyst):
        compare = sorted(lyst)
        if compare == lyst:
            return(True)
        else:
            return(False)
    else:
        raise ValueError("Parameter must be a list and all items in the list must be integers!")


#You must also use the builtin timsort--don't write this one yourself'''

def main():
    random.seed(13)
    lyst = random.sample(range(100000), k=10000)
    setrecursionlimit(10**4)

    quick_lyst = lyst.copy()
    random.shuffle(quick_lyst)

    merge_lyst = lyst.copy()
    random.shuffle(merge_lyst)

    select_lyst = lyst.copy()
    random.shuffle(select_lyst)

    insert_lyst = lyst.copy()
    random.shuffle(insert_lyst)

    tim_lyst = lyst.copy()
    random.shuffle(tim_lyst)

    is_sorted_lyst = lyst.copy()
    random.shuffle(is_sorted_lyst)


    '''Testing is_sorted:
    
    print(is_sorted(is_sorted_lyst))
    is_sorted_lyst.sort()
    print(is_sorted(is_sorted_lyst))'''


    print("Starting selection_sort")
    select_start = time.perf_counter()
    selection_sort(select_lyst)
    select_time = time.perf_counter() - select_start
    print(f"selection_sort duration: {select_time: .4f} seconds.\n")

    print("Starting insertion_sort")
    insert_start = time.perf_counter()
    insertion_sort(insert_lyst)
    insert_time = time.perf_counter() - insert_start
    print(f"insertion_sort duration: {insert_time: .4f} seconds.\n")

    print("Starting mergesort")
    merge_start = time.perf_counter()
    mergesort(merge_lyst)
    merge_time = time.perf_counter() - merge_start
    print(f"mergesort duration: {merge_time: .4f} seconds.\n")

    print("Starting quicksort")
    quick_start = time.perf_counter()
    quicksort(quick_lyst)
    quick_time = time.perf_counter() - quick_start
    print(f"quicksort duration: {quick_time: .4f} seconds.\n")

    print("Starting timsort")
    tim_start = time.perf_counter()
    timsort = sorted(tim_lyst)
    tim_time = time.perf_counter() - tim_start
    print(f"timsort duration: {tim_time: .4f} seconds.")



if __name__ == "__main__":
    main()
