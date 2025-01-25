import argparse
import random

parser = argparse.ArgumentParser(
    prog='arithmetic helper',
    description='produces a two column list of basic arithmetic practice problems')
parser.add_argument('-o', '--operators', help='space delimited list of operators to use')
parser.add_argument('-m', '--max', help='biggest number to use')
args = parser.parse_args()

nums = [x for x in range(0, (int(args.max) if args.max is not None else 10) + 1)]
ops = args.operators.split(' ') if args.operators is not None else ['+']

num_lines_per_op = 16

def get_choices(is_subtraction=False):
    choice_a = random.choice(nums)
    choice_b = random.choice(nums)
    return (choice_a, choice_b) if is_subtraction and choice_a > choice_b else (choice_b, choice_a)

for i in range(num_lines_per_op):
    op1 = random.choice(ops)
    choice_a, choice_b = get_choices(is_subtraction = op1 == '-')
    op2 = random.choice(ops)
    choice_c, choice_d = get_choices(is_subtraction = op1 == '-')
    print('%2d %2s %2d = \t\t%2d %2s %2d =' % (choice_a, op1, choice_b, choice_c, op2, choice_d))
