def count_in_list(lst : range, item : int) -> int:
    """"
    This function counts the number of occurrences of an item in a list.

    Args:
        lst (range): range of numbers.
        item (int): item to count.

    Returns:
        int: number of occurrences of an item in a list.
    """
    return sum(1 for elem in lst if elem == item)
