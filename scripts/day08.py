from collections import Counter
from functools import reduce
import operator


with open("assets/day08.txt") as file:
    boxes = [list(map(int, line.strip().split(","))) for line in file.readlines()]


def dist(pair):
    i, j = pair
    xi, yi, zi = boxes[i]
    xj, yj, zj = boxes[j]
    return (xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2


boxes_count = len(boxes)
pair_limit = 1000
top_n = 3

pairs = [(i, j) for i in range(boxes_count) for j in range(i + 1, boxes_count)]
clusters = [-1 for _ in range(boxes_count)]

ans1, ans2 = None, None

for pair_n, pair in enumerate(sorted(pairs, key=dist)):
    i, j = pair
    match clusters[i], clusters[j]:
        case (-1, -1):
            clusters[i] = clusters[j] = max(clusters) + 1
        case (-1, x) | (x, -1):
            clusters[i] = clusters[j] = x
        case (x, y):
            clusters = [x if c == y else c for c in clusters]

    if pair_n + 1 == pair_limit:
        ans1 = reduce(
            operator.mul,
            [
                occurences
                for _, occurences in Counter(
                    [c for c in clusters if c != -1]
                ).most_common(top_n)
            ],
        )

    if len(set(clusters)) == 1 and clusters[0] != -1:
        ans2 = boxes[i][0] * boxes[j][0]

    if ans1 and ans2:
        break

print("Part 1:", ans1)
print("Part 2:", ans2)
