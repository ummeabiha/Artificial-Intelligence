def count_ears(n):
    if n == 0:
        return 0
    elif n % 2 == 1: #odd
        return 2 + count_ears(n - 1)
    else: #even
        return 3 + count_ears(n - 1)

n = 6  
result = count_ears(n)
print(f"The total number of ears for {n} bunnies is: {result}")
