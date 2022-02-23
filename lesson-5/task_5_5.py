numbers_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

num = {}
for i in numbers_list:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
result = [elem for elem in numbers_list if num[elem] == 1]
print(result)
