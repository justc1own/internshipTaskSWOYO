def prime_numbers(low, high):
    ans = []
    if isinstance(low, int) == False or isinstance(high, int) == False or low <= 0 or high < low:
        return []

    ans.append(2)
    if high == 2:
        return ans

    for i in range(3, high+1):
        f = 1
        for j in ans:
            if i % j == 0:
                f = 0
                break
            if j * j > i:
                break
        if f == True:
            ans.append(i)

    ans = [x for x in ans if x >= low]
    return ans

ans = prime_numbers(1, 20)

print(ans)
assert(prime_numbers(2, 2)) == [2]
assert(prime_numbers(1, 10)) == [2, 3, 5, 7]
assert(prime_numbers(11, 20)) == [11, 13, 17, 19]
assert(prime_numbers(5, 1)) == []
assert(prime_numbers(0, 10)) == [] 
assert(prime_numbers(1, -10)) == []
assert(prime_numbers("1", 10)) == [] 
assert(prime_numbers(1, [10])) == []
assert(len(prime_numbers(1, 100000))) == 9592
