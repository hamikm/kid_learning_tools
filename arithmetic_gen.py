import random

max_num = 5

a = [x for x in range(0, max_num + 1)]
b = [x for x in range(0, max_num + 1)]

ops = ['+']

num_lines_per_op = 15

for op in ops:
    for i in range(num_lines_per_op):
        rand_a = random.choice(a)
        rand_b = random.choice(b)
        print(f'{rand_a} {op} {rand_b} = \t\t\t\t{rand_a} {op} {rand_b} =')
    print()
