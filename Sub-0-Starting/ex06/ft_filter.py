def ft_filter(function, iterable):
    """Immitates the behavior of built in function "filter"

        Takes: Function, Iterable

        Returns: Item"""

    if function:
        return (item for item in iterable if (function(item)))
    return (item for item in iterable if item)
