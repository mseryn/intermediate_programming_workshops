def sort_items_by_color(input_list, color_order = ["red", "orange", "yellow", "green", "blue", "violet"]):
    """
    Function to sort items by color
    Takes:
        List of items
        [Optional] Ordered list of color terms to sort by
    Returns: 
        List of items sorted by colors listed in ordered list
    """

    return [item if item.get_color == color for item in input_list for color in color_order]
