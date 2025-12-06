ranges = []

with open("assets/day05.txt") as file:
    while (line := file.readline()) != "\n":
        ranges.append(list(map(int, line.split("-"))))

ranges = list(sorted(ranges))
outs = []
answer = 0

for start, end in ranges:
    key_numbers = [start, end]

    for start2, end2 in outs:
        if start <= start2 <= end:
            key_numbers.append(start2)
        if start <= end2 <= end:
            key_numbers.append(end2)

    key_numbers = list(sorted(set(key_numbers)))

    if len(key_numbers) == 1:
        if not any(x <= key_numbers[0] <= y for x, y in outs):
            answer += 1

    for a, b in zip(key_numbers, key_numbers[1:]):
        is_a_overlapping = any(x <= a <= y for x, y in outs)
        is_b_overlapping = any(x <= b <= y for x, y in outs)
        overlapping_ends = int(is_a_overlapping) + int(is_b_overlapping)

        if overlapping_ends < 2:
            answer += b - a + (1 - overlapping_ends)

    outs.append((start, end))

print(answer)
