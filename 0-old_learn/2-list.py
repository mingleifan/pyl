trans = ["car", 'airplane', 'ship']
print(trans)

trans.append('bicycle')
print(trans)

trans.insert(0, 'bicycle')
print(trans)

del trans[0]
print(trans)

# print(transportation.pop(0))
# print(transportation.pop())
# print(transportation)

# transportation.remove("airplane")
# print(transportation)

# sort() 永久性排序
trans.sort()
print(trans)

trans.sort(reverse=True)
print(trans)

# sorted() 临时排序
print(sorted(trans))
print(trans)

# reverse() 列表反转
trans.reverse()

# len() 列表长度
print(len(trans))
