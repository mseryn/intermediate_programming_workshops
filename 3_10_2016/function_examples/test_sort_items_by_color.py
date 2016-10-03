import timeit
import random

import better_sort_items_by_color
import commented_list_comprehension_sort_items_by_color
import commented_naive_sort_items_by_color

class ColoredItem():
    def __init__(self, color):
        self._color = color
    def get_color(self):
        return self._color

def random_colored_items(amount):
    items = []
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    for _ in range(amount):
        items.append(ColoredItem(colors[random.randint(0, len(colors) - 1)]))
    return items

if __name__ == "__main__":
    items = random_colored_items(45)

    print("*** Naive Sort ***")

    print("\nUNSORTED ITEMS: \n")
    for item in items:
        print(item.get_color())

    start_time = timeit.default_timer()
    sorted_items = commented_naive_sort_items_by_color.sort_items_by_color(items)    
    total_time = timeit.default_timer() - start_time

    print("\nSORTED ITEMS: \n")
    for item in sorted_items:
        print(item.get_color())
    
    print("\nSORTING TOOK %f SECONDS \n" %(total_time))

    print("*** List Comprehension Sort ***")

    print("\nUNSORTED ITEMS: \n")
    for item in items:
        print(item.get_color())

    start_time = timeit.default_timer()
    sorted_items = commented_list_comprehension_sort_items_by_color.sort_items_by_color(items)    
    total_time = timeit.default_timer() - start_time

    print("\nSORTED ITEMS: \n")
    for item in sorted_items:
        print(item.get_color())
    
    print("\nSORTING TOOK %f SECONDS \n" %(total_time))

    print("*** Better Sort ***")

    print("\nUNSORTED ITEMS: \n")
    for item in items:
        print(item.get_color())

    start_time = timeit.default_timer()
    sorted_items = better_sort_items_by_color.sort_items_by_color(items)    
    total_time = timeit.default_timer() - start_time

    print("\nSORTED ITEMS: \n")
    for item in sorted_items:
        print(item.get_color())
    
    print("\nSORTING TOOK %f SECONDS \n" %(total_time))
