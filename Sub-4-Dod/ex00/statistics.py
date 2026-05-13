def give_mean(num_list, list_len):
    if list_len <= 1:
        print("ERROR")
        return

    mean = sum(num_list) / list_len
    print(f"mean: {mean}")

    return


def give_q2(num_list, list_len):
    if list_len <= 1:
        print("ERROR")
        return

    if (list_len - 1) % 2 == 0:
        q2 = num_list[int((list_len - 1) / 2)]
    else:
        q2 = num_list[int(list_len / 2)]

    print(f"median: {q2}")
    return


def give_q1_q3(num_list, list_len):
    if list_len <= 1:
        print("ERROR")
        return

    q1 = float(num_list[int(list_len / 4)])
    q3 = float(num_list[int((list_len / 4) * 3)])

    print(f"quartile: [{q1}, {q3}]")
    return


def give_std(num_list, list_len):
    if list_len <= 1:
        print("ERROR")
        return

    mean = sum(num_list) / list_len

    sqd = [(x - mean)**2 for x in num_list]
    sqd_sum = sum(sqd)

    var = sqd_sum / list_len

    std = var**0.5
    print(f"std: {std}")
    return


def give_var(num_list, list_len):
    if list_len <= 1:
        print("ERROR")
        return

    mean = sum(num_list) / list_len

    sqd = [(x - mean)**2 for x in num_list]
    sqd_sum = sum(sqd)

    var = sqd_sum / list_len
    print(f"var: {var}")
    return


def ft_statistics(*args: any, **kwargs: any) -> None:

    num_list = [x for x in args]
    num_list.sort()
    list_len = len(num_list)
    # print(list_len)

    values = [value for key, value in kwargs.items()]
    if not values:
        print("ERROR")
    for value in values:
        match value:
            case _ if value == "mean":
                give_mean(num_list, list_len)
            case _ if value == "median":
                give_q2(num_list, list_len)
            case _ if value == "quartile":
                give_q1_q3(num_list, list_len)
            case _ if value == "std":
                give_std(num_list, list_len)
            case _ if value == "var":
                give_var(num_list, list_len)
            case _:
                pass
