def sort_items_by_color(input_list, color_order = ["red", "orange", "yellow", "green", "blue", "violet"]):
    return_list = []
    for color in color_order:
        for item in input_list:
            if item.get_color == color:
                return_list.append(item)
    return return_list
