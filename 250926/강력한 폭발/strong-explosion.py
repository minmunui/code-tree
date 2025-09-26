import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

pos_bomb = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            pos_bomb.append((i, j))

n_bomb = len(pos_bomb)

init = []
maxima = 0

def print_area(a):
    for row in a:
        for i in row:
            print(f"{i}", end=" ")
        print()


def get_area(bombs: list[int]):
    _grid = copy.deepcopy(grid)
    # print(f"bombs : {bombs}")

    temp_grid = [[0] * n for _ in range(n)]
    bombed = set()

    for i, bomb in enumerate(bombs):
        
        pos = pos_bomb[i]
        _grid[pos[0]][pos[1]] = bomb
        if bomb == 1:
            _bombed = [pos, (pos[0] - 1, pos[1]), (pos[0] - 2, pos[1]), (pos[0] + 1, pos[1]), (pos[0] + 2, pos[1])]
        if bomb == 2:
            _bombed = [pos, (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1)]
        if bomb == 3:
            _bombed = [pos, (pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1)]
        
        bombed = bombed.union(_bombed)

        # print(f"temp : {temp_grid}")

        # print(f"bombed : {bombed}")
    result = [ e for e in bombed if (0 <= e[0] < n) and (0 <= e[1] < n)]

    # print("bombs")
    # print_area(_grid)
    # print("bombed_area")
    # print_area(temp_grid)
    # print()
    return len(result)


def choose(arr):
    global maxima

    if len(arr) >= n_bomb:
        maxima = max(maxima, get_area(arr))
        return

    else:
        for i in range(1, 4):
            arr.append(i)
            choose(arr)
            arr.pop()

choose([])

print(maxima)