n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
maxima = 99999

def jump(pos, count):
    """점프!"""
    # print(f"jump({pos}, {count})")
    global num, n, maxima
    if pos == n:
        if maxima > count:
            maxima = count
        return

    if count >= maxima:
        return

    for candid in range(1, num[pos] + 1):
        next_pos = pos + candid
        jump(next_pos, count + 1)

jump(1, 0)

if maxima == 99999:
    print(-1)
else:
    print(maxima)