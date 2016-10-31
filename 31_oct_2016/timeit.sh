#!/bin/bash

python -m timeit -s "import merge_sort" "alist = [54,26,93,17,77,31,44,55,20]" "merge_sort.mergeSort(alist)"

python -m timeit -s "import insertion_sort" "alist = [54,26,93,17,77,31,44,55,20]" "insertion_sort.insertionSort(alist)"

python -m timeit -s "import counting_sort" "alist = [54,26,93,17,77,31,44,55,20]" "counting_sort.countingSort(alist, 100)"
