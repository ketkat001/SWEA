def fact_num(n):
    if n == 1:
        fact[n] = 1
    elif fact_num(n-1) == 0:
        return n * fact_num(n-1)
    else:
        fact[n] = n * fact[n-1]


fact = [0] * 17
for i in range(1, 17):
    fact_num(i)
result = [0]
T = int(input())
for _ in range(T):
    