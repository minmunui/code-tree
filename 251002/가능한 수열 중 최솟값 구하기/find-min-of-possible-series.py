n = int(input())

# Please write your code here.

results = []
candids = [4, 5, 6]

def get_valid_candids(cur):
    """현재 cur에서 다음으로 올 수 있는 숫자들을 반환"""
    if len(cur) == 0:
        return candids
    
    return [val for val in candids if valid(cur + [val])]

def valid(arr):
    # print(f"arr = {arr}")
    """현재 arr이 가능한지 확인"""
    for i in range(1, len(arr) // 2 + 1):
        current = arr[-i : ]
        last = arr[-i * 2 : -i]
        # print(f"{i} : {current} | {last}")
        if current == last:
            return False
    return True


def choose(cur):
    global n
    # 불가능한 숫자 폐기

    if len(cur) == n:
        results.append(cur)
        return True
    
    else:
        for val in get_valid_candids(cur):
            cur = cur + [val]
            found = choose(cur)
            if found:
                return True
            cur = cur[:-1]


choose([])

for char in results[0]:
    print(char, end="")
