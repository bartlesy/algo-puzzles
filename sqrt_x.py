# https://leetcode.com/problems/sqrtx/description/

def mySqrt(x):
    if x <= 1:
        return x
    y = x if x < 4 else x // 2
    low = 0
    high = y
    while int(y * y) != x:
        if (y * y) > x:
            high = y
            y = (y + low) / 2
        elif (y * y) < x:
            low = y
            y = (y + high) / 2
        elif (y * y) == x:
            break
    return int(y)




if __name__ == '__main__':
    print(mySqrt(4) == 2)
    print(mySqrt(8) == 2)
    print(mySqrt(2))
    print(mySqrt(5))

