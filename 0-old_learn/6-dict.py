person = {"name": "lange", "age": 23, "sex": "man"}

print(person.get("name"))
print(person['name'])

person['school'] = 'SC UNIVERSITY'
print(person)

person['age'] = person['age'] + 1
print(person)

# 删除键值对
del person['school']
print(person)

# 遍历字典
for k, v in person.items():
    print(k + ":" + str(v))

print("-----------------")

# 遍历键

for k in person.keys():
    print(k.title())
    print(k)

# 按顺序遍历
people = [{'name': 'lange', 'age': 24}, {'name': 'fml', 'age': 23}, {'name': 'wyf', 'age': 22}]

for p in sorted(people, key=lambda x: x['age']):
    print(p)
