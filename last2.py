def last2(str):
    last_2 = str[-2:]
    cnt = 0
    for c1, c2 in zip(str[:-2], str[1:-1]):
        if "%s%s" % (c1, c2) == last_2:
            cnt += 1
    return cnt
