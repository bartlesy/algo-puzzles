def skip_identical(lst):
    """ Print output as shown below.

    list_description = [('name1','species','description','country','n/a'),
                        ('name1','species','description','country','plasmid1'),
                        ('name1','species','description','country','plasmid2')]

    >>> skip_identical(list_description)
    name1 species description country n/a
                                      plasmid1
                                      plasmid2
    """
    for row, prev_row in zip(lst, [["filler" for _ in lst[0]]] + lst):
        format_args = [
            ele if ele != prev_ele else " " * len(ele)
            for ele, prev_ele in zip(row, prev_row)
        ]
        print("\t".join(format_args))
    return

    # your code here


list_description = [
    ("name1", "species", "description", "country", "n/a"),
    ("name1", "species", "description", "country", "plasmid1"),
    ("name1", "species", "description", "country", "plasmid2"),
]

skip_identical(list_description)
