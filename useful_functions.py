def sum_of_values(*values):
    """Get a sequence of values or a sequence of sequence of values
    and returns the sum all values.
    The following are valid calls to this function:
        sum_of_values(1, 2, 3, 4) --> 10
        sum_of_values([1, 2, 3, 4]) --> 10
        sum_of_values(*[1, 2, 3, 4]) --> 10
        sum_of_values([1, 2], 3, 4) --> 10
        sum_of_values(k for k in range(1, 5)) --> 10
    """
    _sum = 0
    for value in values:
        try:
            _sum += value
        except TypeError:
            _sum += sum_of_values(*(k for k in value))
    return _sum


def get_median(values):
    """Get a sequence of values and returns the median of this values
    Args:
        - values: a list of numeric values
    Returns:
        - The median of provided values.
    """
    size = len(values)
    midle = size // 2
    if size % 2:
        return values[midle]
    return (values[midle] + values[midle - 1]) / 2
