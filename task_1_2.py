cube_numbers = []

for n in range(0, 1001):
    if n % 2:
        n = n ** 3
        cube_numbers.append(n)

for idx in range(len(cube_numbers)):
    sum_numbers = 0
    m = cube_numbers[idx]
    while m:
        sum_numbers += m % 10
        m = m // 10
    if sum_numbers % 7 == 0:
        sum_all_numbers = 0
        sum_all_numbers += cube_numbers[idx]
    cube_numbers[idx] += 17
    sum_numbers = 0
    m = cube_numbers[idx]
    while m:
        sum_numbers += m % 10
        m = m // 10
    if sum_numbers % 7 == 0:
        sum_all_numbers17 = 0
        sum_all_numbers17 += cube_numbers[idx]

print(sum_all_numbers)
print(sum_all_numbers17)