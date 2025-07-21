print("------- for -------")
names = ['A', 'B', 'C']
for name in names:
    print(name)
print("-----------------")
total_sum = 0
for i in [1, 2, 3, 4, 5, 6]:
    total_sum += i
print(total_sum)
print("-----------------")
total_sum = 0
for i in range(101):
    total_sum += i
print(total_sum)
print("-----------------")

for x in range(1, 10, 2):
    print(x)

print("------- while -------")
n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
print("-----------------")
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
