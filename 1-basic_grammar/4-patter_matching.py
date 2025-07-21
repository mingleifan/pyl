score = 'B'
match score:
    case 'A':
        print('Excellent')
    case 'B':
        print('Good')
    case 'C':
        print('Fair')
    case 'D':
        print('Poor')
    case _:
        print('Invalid Score')

age = 15
match age:
    case x if x < 10:
        print(x)
    case 10:
        print('10 years old')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11 ~ 18 years old')
    case 19:
        print('19 years old')
    case _:
        print('Not sure')
print("x:", x)

args = ['gcc', 'hello.c', 'world.c', 'x.c']
match args:
    case ['gcc']:
        print('gcc: missing source file(s).')
        # 出现gcc，且至少指定了一个文件:
    case['gcc', file1, *files]:
        print('gcc compile: ' + file1 + '; ' + ', '.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('Invalid command...')
