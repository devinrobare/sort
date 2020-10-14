# sort
Testing different sorting algorithms to see which are most efficient

This was a project for school. The purpose was to implement 4 different types of sorting algorithms and compare how fast they were.

The different sort algorithms were quicksort, mergesort, selection sort, and insertion sort.

Quicksort uses a recursive "divide and conquer" method. A number is chosen as the pivot (in this project, the length of the list divided by 2) 
and the list is split into 2 smaller lists based on that index. The process is then repeated on each half, recursively, as the values are swapped to put them in order.

Mergesort also uses recursion to "divide and conquer". The list is split in half and mergesort is called on each half recursively. 
The lists are then merged back together in the correct order.

Selection sort iterates through the list looking for the smallest element and places it at the beginning of the list. 
It then looks for the next smallest number and moves it to the second spot in the list. This repeats until all elements are sorted.

Insertion sort moves through the list by taking the first number and comparing it to the next. If it's less, it's moved to the left of the start number. 
This continues through the list, with each number being compared and, if less than the comparing number, are moved to the left and re-compared with the
numbersto the left of that until they reach a number that's smaller. They are then "inserted" to the right of that smaller number.

I used the random module to create a large, shuffled list for testing, then copied that list so each sort function could be tested.
I used the time.perf_counter() to time each function.

Quicksort and mergesort both utilize recursion, and the project required a recursion counter for grading purposes. 
I commented this out since the recursion counter was not my own code. 
I also commented out aother piece required for the project, my is_sorted test function that determines if my functions are sorting correctly.
