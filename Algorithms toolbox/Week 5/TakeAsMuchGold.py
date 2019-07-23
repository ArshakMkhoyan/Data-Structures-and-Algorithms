W, n = map(int, input().split())
ws = list(map(int, input().split()))

dmat = [[0 for i in range(W + 1)] for k in range(n + 1)]

for gold in range(1, n + 1):
    for weight in range(1, W + 1):
        dmat[gold][weight] = dmat[gold - 1][weight]
        if ws[gold - 1] <= weight:
            val = dmat[gold - 1][weight - ws[gold - 1]] + ws[gold - 1]
            if val > dmat[gold][weight]:
                dmat[gold][weight] = val
print(*dmat, sep='\n')

# T = {}
# def rec(w, choice):
#     a = choice
#     if w not in T:
#         if w == 0:
#             T[w] = 0
#         maximum = 0
#         for gold in ws:
#             if gold <= w and (gold not in a):
#                 maximum = max(maximum, rec(w - gold, a.add(gold)) + gold)
#         T[w] = maximum
#     return T[w]
#
# print(rec(W, set()))
