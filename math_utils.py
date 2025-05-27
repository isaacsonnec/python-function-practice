def summation(n):
    return sum(range(1, n+1))

def summation_2(n):
    summation = 0
    for i in range (n+1):
        summation += i
    return summation
