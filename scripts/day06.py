from functools import reduce
from itertools import groupby
import operator

ops = {"+": operator.add, "*": operator.mul}

with open("assets/day06.txt") as file:
    lines = file.readlines()

# Part 1: parse numbers, then transpose
numbers1 = [*zip(*[map(int, line.split()) for line in lines[:-1]])]
# Part 2: transpose raw lines, then merge digits, group numbers by empty column, then parse
numbers2 = [*zip(*lines[:-1])]
numbers2 = [reduce(operator.add, row).strip() for row in numbers2]
numbers2 = [list(map(int, g)) for k, g in groupby(numbers2, key=bool) if k]

operations = list(map(ops.get, lines[-1].split()))

for part, numbers in (("1", numbers1), ("2", numbers2)):
    ans = sum(
        reduce(operation, operands) for operation, operands in zip(operations, numbers)
    )
    print(f"Part {part}:", ans)
