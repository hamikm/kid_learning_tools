import random

max_num = 10

nums = [x for x in range(0, max_num + 1)]

ops = ['-']

num_lines_per_op = 16

def get_choices():
    choice_a = random.choice(nums)
    choice_b = random.choice(nums)
    return (choice_a, choice_b) if op == '-'and choice_a > choice_b else (choice_b, choice_a)

for op in ops:
    for i in range(num_lines_per_op):
        choice_a, choice_b = get_choices()
        choice_c, choice_d = get_choices()
        print('%2d %2s %2d = \t\t%2d %2s %2d =' % (choice_a, op, choice_b, choice_c, op, choice_d))
    print()
