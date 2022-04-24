''' Euler 01 '''

p0 = []
p1 = []
p2 = []


# def uso(valor):
#     if valor % 3 == 0 or valor % 5 == 0:
#         return valor
#     return 0


# for n in [12]:
#     soma = 0
#     print('n =', n)
#     print('n/2 =', n/2)
#     if n == 0:
#         pass
#     else:
#         for item in range(int(n//2)):
#             p0.append(item)
#             p0.append(int(n/2+item))

#             soma += uso(item)
#             p1.append(item)

#             soma += uso(n//2+item)
#             p2.append(int(n/2+item))

#     if n % 2 != 0:
#         soma += uso(n)
#         p2.append(n)

#     print(soma)

# print("p0:", p0, len(p0))
# print("p1:", p1)
# print("p2:", p2)

def uso(valor):
    if valor % 3 == 0 or valor % 5 == 0:
        return valor
    return 0


for n in [-1, 10, 100, 10000]:
    soma = 0
    if n == 0:
        pass
    else:
        for item in range(int(n//2)):
            soma += uso(item)
            soma += uso(n//2+item)
    
    if n % 2 != 0:
        soma += uso(n)
    print(soma)




# for n in [0,10,100,1000]:
#     soma = 0
#     if n == 0:
#         pass
#     else:
#         for item in range((n)):
#             if item % 3 == 0 or item % 5 == 0:
#                 soma += item
#         print(soma)


# print('*'*80)
# for n in [10,100]:
#     soma = 0
#     if n == 0:
#         pass
#     else:
#         for item in range(0, n, 3):
#             if item % 5 != 0:
#                 soma += item
#         for item in range(0, n, 5):
#             soma += item
#     print(soma)

