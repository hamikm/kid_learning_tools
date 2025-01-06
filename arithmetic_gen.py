import random

max_num = 6

a = [x for x in range(0, max_num + 1)]
b = [x for x in range(0, max_num + 1)]

ops = ['+']

num_lines_per_op = 15

for op in ops:
    for i in range(num_lines_per_op):
        print(f'{random.choice(a)} {op} {random.choice(a)} = \t\t\t\t{random.choice(a)} {op} {random.choice(a)} =')
    print()
