print("------- dict -------")
d = {'Michal': 90, 'Rango': 99, 'Bob': 78}
print(d)
# 设置值
d['Lisa'] = 66
print(d)
# var = d['Tomas']
var = d.get('Tomas', 0)  # get or default
print(var)
bobV = d.pop('Bob')
print(bobV)
print(d)

print("------- set -------")
s1 = {1, 2, 3}
print('s1: %s' % s1)
l1 = [3, 4, 5]
s2 = set(l1)
print('s2:', s2)

s1.add(4)
s1.remove(2)
print('s1:', s1)

s3 = s1 & s2
print('s3:', s3)

s4 = s1 | s2
print('s4:', s4)

l1.sort(reverse=True)
print(l1)
