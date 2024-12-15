y = int(input())
z = int(input())

additional_days = 0
for i in range(y, z + 1):
    if i % 4 == 0:
        additional_days += 1
    if i % 4 == 0 and i % 100 == 0:
        additional_days -= 1
    if i % 4 == 0 and i % 400 == 0:
        additional_days += 1
print(365 * (z + 1 - y) + additional_days)       