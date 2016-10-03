def sort_items_by_color(input_list, color_order = ["red", "orange", "yellow", "green", "blue", "violet"]):
    """
    Function to sort items by color
    Takes:
        List of items
        [Optional] Ordered list of color terms to sort by
    Returns: 
        List of items sorted by colors listed in ordered list
    """

    return_list = []
    items_by_color = {}

    for color in color_order:
        items_by_color[color] = []
    
    for item in input_list:
        items_by_color[item.get_color()].append(item)

    for color in color_order:
        return_list.extend(items_by_color[color])

    return return_list
