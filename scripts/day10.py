from dataclasses import dataclass
from functools import cache

import numpy as np
from scipy.optimize import linprog
from sklearn.preprocessing import MultiLabelBinarizer


@dataclass(frozen=True)
class Machine:
    lights: tuple[bool]
    buttons: tuple[tuple[int]]
    joltages: tuple[int]


machines: list[Machine] = []

with open("assets/day10.txt") as file:
    lines = file.readlines()

    for line in lines:
        lights = tuple(
            map(
                {".": False, "#": True}.get, line[line.index("[") + 1 : line.index("]")]
            )
        )
        buttons = line[line.index("]") + 2 : line.index("{") - 1]
        buttons = tuple(
            [tuple([int(n) for n in b[1:-1].split(",")]) for b in buttons.split(" ")]
        )
        joltages = line[line.index("{") + 1 : line.index("}")]
        joltages = tuple([int(n) for n in joltages.split(",")])
        machines.append(Machine(lights, buttons, joltages))


# Part 1
def switch(current_lights: tuple[bool], button: tuple[int]):
    return tuple([not x if i in button else x for i, x in enumerate(current_lights)])


@cache
def min_moves(machine: Machine, button_states: tuple[bool]):
    current_lights = tuple(False for _ in machine.lights)

    for button_idx, is_enabled in enumerate(button_states):
        if is_enabled:
            current_lights = switch(current_lights, machine.buttons[button_idx])

    if current_lights == machine.lights:
        return 0

    options = [
        tuple(button_states[:i] + (True,) + button_states[i + 1 :])
        for i in range(len(button_states))
        if not button_states[i]
    ]

    return min(
        [1 + min_moves(machine, buttons) for buttons in options] + [float("inf")]
    )


ans1 = sum(
    [min_moves(m, tuple([False for _ in range(len(m.buttons))])) for m in machines]
)

print("Part 1:", ans1)


# Part 2
ans2 = 0

for machine in machines:
    c = np.ones(len(machine.buttons), dtype=np.int32)
    b_eq = np.array(machine.joltages)
    A_eq = MultiLabelBinarizer().fit_transform(machine.buttons).T

    sln = linprog(c=c, A_eq=A_eq, b_eq=b_eq, integrality=np.ones_like(c))

    ans2 += round(sln.fun)

print("Part 2:", ans2)
