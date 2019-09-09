import itertools


def sort_cartesian_product(list_one, list_two):
    """ Return sorted Cartesian product.

    >>> Cartesian product([1, 5, 6], [0, 3, 7])
    [[0, 1], [1, 3], [1, 7], [0, 5], [3, 5], [5, 7], [0, 6], [3, 6], [6, 7]]
    """
    list_one.sort()
    list_two.sort()
    return [sorted([x, y]) for x in list_one for y in list_two]
    # I feel like this should be the answer since it puts [0, 5] before [1, 3]
    # not sure what the sort func is supposed to be
    # return sorted([sorted([x, y]) for x in list_one for y in list_two], key=lambda x: x[0])


# Do not make any changes to the code below
# Function used in main() to print
# what each function returns vs. what it's supposed to return


def test(returned, expected):
    if returned == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print(
        "{0} returned: {1} expected: {2}".format(
            prefix, repr(returned), repr(expected)
        )
    )


# Do not make any changes to the code below
# Calls the above functions with interesting inputs.
def main():
    print("sort_cartesian_product")
    test(
        sort_cartesian_product([1, 5, 6], [0, 3, 7]),
        [
            [0, 1],
            [1, 3],
            [1, 7],
            [0, 5],
            [3, 5],
            [5, 7],
            [0, 6],
            [3, 6],
            [6, 7],
        ],
    )


if __name__ == "__main__":
    main()
