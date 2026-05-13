def square(x: int | float) -> int | float:
    sq = x ** 2
    return sq


def pow(x: int | float) -> int | float:
    pw = x ** x
    return pw


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        base = function(x)
        for i in range(count):
            base = function(base)
        count += 1
        return base
    return inner
