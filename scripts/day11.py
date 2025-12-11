from collections import defaultdict
from functools import cache

graph = defaultdict(set)

with open("assets/day11.txt") as file:
    graph.update(
        {
            nodes[0][:-1]: set(nodes[1:])
            for nodes in [line.strip().split() for line in file.readlines()]
        }
    )


def find_paths(graph: dict, fr: str, to: str):
    paths = set()

    @cache
    def dfs(visited: tuple[str]):
        if visited[-1] == to:
            paths.add(visited)
        to_visit = {n for n in graph[visited[-1]] if n not in visited}
        if not to_visit:
            return
        for n in to_visit:
            dfs((*visited, n))

    dfs((fr,))
    return paths


ans1 = len(find_paths(graph, "you", "out"))
print("Part 1:", ans1)
