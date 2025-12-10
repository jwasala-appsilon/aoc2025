from tqdm import tqdm


with open("assets/day09.txt") as file:
    reds = [tuple(map(int, line.strip().split(","))) for line in file.readlines()]


def area(pair):
    i, j = pair
    xi, yi = reds[i]
    xj, yj = reds[j]
    return (abs(xi - xj) + 1) * (abs(yi - yj) + 1)


n = len(reds)
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
ans1 = max(map(area, pairs))

outer = []

for (x1, y1), (x2, y2) in zip(reds, reds[1:] + [reds[0]]):
    if x1 == x2:
        outer += [(x1, y) for y in (range(y1, y2) or range(y1, y2, -1))]
    elif y1 == y2:
        outer += [(x, y1) for x in (range(x1, x2) or range(x1, x2, -1))]
    else:
        raise NotImplementedError


def is_eligible(pair):
    i, j = pair
    xi, yi = reds[i]
    xj, yj = reds[j]

    x_min = min(xi, xj)
    x_max = max(xi, xj)
    y_min = min(yi, yj)
    y_max = max(yi, yj)

    return not any((x_min < xk < x_max) and (y_min < yk < y_max) for xk, yk in outer)


for pair in tqdm(sorted(pairs, key=area, reverse=True)):
    if is_eligible(pair):
        ans2 = area(pair)
        break

print("Part 1:", ans1)
print("Part 2:", ans2)
