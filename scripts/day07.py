from collections import defaultdict
from functools import cache


with open("assets/day07.txt") as file:
    lines = [list(line.strip()) for line in file.readlines()]

# Prep: parse the manifold as a graph where each position of the beam is a node
# and each movement is an edge (including both splits and straightforward movements)
nodes = set()
edges = defaultdict(list)

for i, (line, next_line) in enumerate(zip(lines, lines[1:])):
    for j in range(len(line)):
        match line[j], next_line[j]:
            case (("|" | "S"), ("." | "|")):
                next_line[j] = "|"
                edges[(i, j)].append((i + 1, j))
            case ("|", "^"):
                for k in (j - 1, j + 1):
                    if next_line[k] != "^":
                        next_line[k] = "|"
                        edges[(i, j)].append((i + 1, k))
        if line[j] == "|":
            nodes.add((i, j))

# Part 1: the answer is the number of edges excluding straightforward movements
ans1 = sum(
    map(bool, [[n for n in next if n[1] != prev[1]] for prev, next in edges.items()])
)

# Part 2: the answer is the number of exhaustive paths in the graph
root = {n for n in nodes if n[0] == 1}.pop()


@cache
def dfs(root):
    if not edges[root]:
        return 1
    return sum(dfs(next) for next in edges[root])


ans2 = dfs(root)

print("Part 1:", ans1)
print("Part 2:", ans2)
