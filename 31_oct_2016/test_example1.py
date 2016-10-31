import coefficient_example_1
import random

ARRAY1 = [random.random() for _ in range(0, 10000)]
ARRAY2 = [random.random() for _ in range(0, 10000)]

def slow_test():
    coefficient_example_1.slow_processing(ARRAY1, ARRAY2)
    return True

def fast_test():
    coefficient_example_1.faster_processing(ARRAY1, ARRAY2)
    return True

