# Make a function that gets the product of two arrays as A[i] * B[i] and 
# then adds on some random number between 0 and 1 to each product.

import random

def slow_processing(array1, array2):
    # This is O(2n) 
    return_array = []

    if len(array1) != len(array2):
        print("error - must be same length.")
        return None
    else:
        for i in range(0, len(array1)):
            return_array.append(array1[i] * array2[i])

        for j in range(0, len(array2)):
            return_array[j] += random.random()

        return return_array


def faster_processing(array1, array2):
    # This is O(n)
    return_array = []
    
    if len(array1) != len(array2):
        print("error - must be same length.")
        return None
    else:
        for i in range(0, len(array1)):
            return_array.append(array1[i] * array2[i] + random.random())

        return return_array

