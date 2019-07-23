m = int(input())
result = 0
for i in [10, 5, 1]:
    result += m//i
    m = m%i
print(result)