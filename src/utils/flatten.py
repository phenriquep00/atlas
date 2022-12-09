def flatten(l):
    """transforms a list of lists in a single list 

    Args:
        l (list): a list object, populated with other lists

    Returns:
        list: returns a single list with separetted items
    """
    return [item for sublist in l for item in sublist]
