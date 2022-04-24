''' Euler 01 '''
# Por PA e PG

# https://medium.com/@TheZaki/project-euler-1-multiples-of-3-and-5-c24cb64071b0


def soma(n, k):
    d = n // k
    return k * (d * (d+1)) // 2


def euler1(n):
    return soma(n, 3) + soma(n, 5) - soma(n, 15)


t1 = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000002, 1000000005]
# t1 = [2, 10, 100, 105, 1000000000]
for n in t1:
    # n = int(input().strip())
    print(euler1(n - 1))

# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print(euler1(n - 1))