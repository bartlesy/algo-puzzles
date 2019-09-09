#!/usr/bin/env python3
import random


def naive_algo(in_arr):
    """
    this is how i implemented it
    tbh I still dont grok WHY it's wrong
    but i get HOW it's wrong
    """
    for i, x in enumerate(in_arr):
        idx2 = random.randint(0, len(in_arr) - 1)
        in_arr[i], in_arr[idx2] = in_arr[idx2], x
    return in_arr


def knuth_shuffle(in_arr):
    for i in range(len(in_arr) - 1, -1, -1):
        idx2 = random.randint(0, i)
        in_arr[i], in_arr[idx2] = in_arr[idx2], in_arr[i]
    return in_arr


if __name__ == "__main__":
    print(naive_algo(list(range(10))))
    print(knuth_shuffle(list(range(10))))
