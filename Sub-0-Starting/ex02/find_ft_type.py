def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List :", object.__class__)
    elif isinstance(object, tuple):
        print("Tuple :", object.__class__)
    elif isinstance(object, set):
        print("Set :", object.__class__)
    elif isinstance(object, dict):
        print("Dict :", object.__class__)
    elif isinstance(object, str) and object == "Brian":
        print("Brian is in the kitchen :", object.__class__)
    elif isinstance(object, str) and object == "Toto":
        print("Toto is in the kitchen :", object.__class__)
    else:
        print("Type not found")
    return 42
