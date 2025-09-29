n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

DIRECTION = {
    1 : (-1, 0),
    2 : (-1, 1),
    3 : (0, 1),
    4 : (1, 1),
    5 : (1, 0),
    6 : (1, -1),
    7 : (0, -1),
    8 : (-1, -1)
}

# Please write your code here.
num_move = 0

def get_movable_pos(pos:list[int, int]):
    direction = move_dir[pos[0]][pos[1]]
    # print(f"pos : {pos}")
    cur_pos = [pos[0] + DIRECTION[direction][0], pos[1] + DIRECTION[direction][1]]

    result = []
    while 0 <= cur_pos[0] < n and 0 <= cur_pos[1] < n:
        # print(f"cur_pos : {cur_pos}")
        if num[cur_pos[0]][cur_pos[1]] > num[pos[0]][pos[1]]:
            result.append(cur_pos)
        cur_pos = [cur_pos[0] + DIRECTION[direction][0], cur_pos[1] + DIRECTION[direction][1]]
    return result


maxima = []
current = []

def choose(pos):
    global current, maxima
    movable = get_movable_pos(pos)

    if len(movable) == 0:
        return

    for m in movable:
        current = current + [m]
        if len(maxima) < len(current):
            maxima = current
        choose(m)
        current = current[:-1]

choose([r-1, c-1])
print(len(maxima))