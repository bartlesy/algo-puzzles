import functools

@functools.lru_cache()
def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def main(tar=4e6):
    cur_sum = 0
    i = 0
    while fibo(i) <= tar:
        fx = fibo(i)
        if not fx % 2:
            cur_sum += fx
        i += 1
    return cur_sum


if __name__ == '__main__':
    print(main())
