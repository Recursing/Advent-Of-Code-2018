from dataclasses import dataclass
import re
@dataclass
class Rectangle:
    claim_id : int
    x : int
    y : int
    width : int
    height : int

lines = open('data.txt','r').readlines()
line_format = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
parsed = [map(int, re.match(line_format, line).groups()) for line in lines]
rectangles = [Rectangle(*line) for line in parsed]

# Assumes ids > 0, could use strings
FREE, SHARED = 0, -1
used = [FREE for i in range(1000 * 1000)]
overlaps = {r.claim_id:False for r in rectangles}
for r in rectangles:
    for x in range(r.x, r.x + r.width):
        for y in range(r.y, r.y + r.height):
            cell_id = y * 1000 + x
            if used[cell_id] != FREE:
                overlaps[r.claim_id] = True
                if used[cell_id] != SHARED:
                    overlaps[used[cell_id]] = True
                    used[cell_id] = SHARED
            else:
                used[cell_id] = r.claim_id

print(sum(c == SHARED for c in used))
print(next(claim_id for claim_id, s in overlaps.items() if not s))
