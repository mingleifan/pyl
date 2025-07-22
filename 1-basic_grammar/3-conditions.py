print('--------lean conditions---------')

age = 20
print('your age is', age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('child')

name = input('please input your name:')
ageStr = input('please input your age:')
print('hello,', name)
age = int(ageStr)
if age >= 18:
    print('you are an adult')
elif age >= 6:
    print('you are a teenager')
else:
    print('you are a child')

height = 1.75
weight = 80.5
bmi_val = weight / (height ** 2)
print('bmi_val:%.2f' % bmi_val)
if bmi_val > 32:
    print('严重肥胖')
elif 28 <= bmi_val < 32:
    print('肥胖')
elif 25 <= bmi_val < 28:
    print('过重')
elif 18.5 <= bmi_val < 25:
    print('正常')
elif bmi_val < 18.5:
    print('过轻')
else:
    print('error')
