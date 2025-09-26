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

    for i, bomb in enumerate(bombs):
        
        pos = pos_bomb[i]
        _grid[pos[0]][pos[1]] = bomb
        if bomb == 1:
            bombed = [pos, (pos[0] - 1, pos[1]), (pos[0] - 2, pos[1]), (pos[0] + 1, pos[1]), (pos[0] + 2, pos[1])]
        if bomb == 2:
            bombed = [pos, (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1)]
        if bomb == 3:
            bombed = [pos, (pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1)]
        

        # print(f"temp : {temp_grid}")

        # print(f"bombed : {bombed}")
        for _bombed in bombed:
            if (0 <= _bombed[0] < n) and (0 <= _bombed[1] < n):
                temp_grid[_bombed[0]][_bombed[1]] = 1

    # print("bombs")
    # print_area(_grid)
    # print("bombed_area")
    # print_area(temp_grid)
    # print()
    result = sum([a.count(1) for a in temp_grid])
    return result


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