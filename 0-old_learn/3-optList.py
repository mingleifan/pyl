# 循环
names = ['Hulk', 'Stark', 'Thor', 999]

for name in names:
    print(name)

# range() 左包含 右不包含
for mathVal in range(0, 5):
    print(mathVal)

numbers = list(range(0, 4))
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 列表解析
newNumbers = [value ** 2 for value in range(0, 10)]
print(newNumbers)

# 切片
print(newNumbers[1:4])
print(newNumbers[:4])
print(newNumbers[4:])
# 最后三个
print(newNumbers[-3:])

# 复制
foods = ["1", "2", "3"]

foods2 = foods[:]
foods2.insert(0, "999")

print(foods)
print(foods2)
