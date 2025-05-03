import argparse
import random

parser = argparse.ArgumentParser(
    prog='arithmetic helper',
    description='produces a two column list of basic arithmetic practice problems')
parser.add_argument('-o', '--operators', help='space delimited list of operators to use')
parser.add_argument('-m', '--max', help='biggest number to use')
parser.add_argument('-x', '--multiple', help='multiples of... e.g. 10 or 100')
args = parser.parse_args()

maxMultiple = int(args.multiple) if args.multiple is not None else 1
startingNums = [x for x in range(0, (int(args.max) if args.max is not None else 10) + 1)]
ops = args.operators.split(' ') if args.operators is not None else ['+']

multiple = maxMultiple
nums = []
while (multiple > 1):
    nums.extend([x * multiple for x in startingNums])
    multiple /= 10

num_lines_per_op = 20

def get_choices(is_subtraction=False):
    choice_a = random.choice(nums)
    choice_b = random.choice(nums)
    return (choice_a, choice_b) if is_subtraction and choice_a > choice_b else (choice_b, choice_a)

for i in range(num_lines_per_op):
    op1 = random.choice(ops)
    choice_a, choice_b = get_choices(is_subtraction = op1 == '-')
    op2 = random.choice(ops)
    choice_c, choice_d = get_choices(is_subtraction = op2 == '-')
    print('%3d %2s %3d = \t  %3d %2s %3d =' % (choice_a, op1, choice_b, choice_c, op2, choice_d))
