def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, object.__class__)
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, object.__class__)
    elif isinstance(object, bool) and object is False:
        print("Fake:", object, object.__class__)
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, object.__class__)
    elif isinstance(object, str) and object == "":
        print("Empty:", object, object.__class__)

    else:
        print("Type not found")
        return 1
    return 0
