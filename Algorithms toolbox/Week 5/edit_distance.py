str1 = input()
str2 = input()

dynm = [[0 for i in range(len(str1) + 1)] for k in range(len(str2) + 1)]
for i in range(len(str1) + 1):
    dynm[0][i] = i
for i in range(len(str2) + 1):
    dynm[i][0] = i

for row in range(1, len(str2) + 1):
    for col in range(1, len(str1) + 1):
        dynm[row][col] = min(dynm[row - 1][col] + 1, dynm[row][col - 1] + 1,
                             dynm[row - 1][col - 1] + (str1[col - 1] != str2[row - 1]))
# print(*dynm, sep='\n')
print(dynm[-1][-1])
