n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

lines = list(zip(x1, x2))

def is_selectable(ls):
    # print(f"is_selectable({ls})")
    grid = [0] * 1001
    for l in ls:
        for point in range(l[0], l[1]+1):
            grid[point] += 1
        # print(grid)
        if 2 in grid:
            return False
    return True


combs = []

def make_comb(lines):
    global combs

    def backtrack(start_idx, current):
        combs.append(current)
        for i in range(start_idx, len(lines)):
            backtrack(i + 1, current + [lines[i]])

    backtrack(0, [])

make_comb(lines)
combs.sort(lambda x : len(x))
combs = list(reversed(combs))

def main():
    for line in combs:
        if is_selectable(line):
            print(len(line))
            return

main()