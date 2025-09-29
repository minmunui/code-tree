K, N = map(int, input().split())

# Please write your code here.
def selectable(arr:list[int], item:int):
    if len(arr) < 2:
        return True
    else:
        return not(item == arr[-1] and item == arr[-2])

results = []

def choose(cur):
    # print(f"cur : {cur}")
    if len(cur) == N:
        # print(f"selected !")
        results.append(cur)
        return
    
    for i in range(1, K+1):
        if selectable(cur, i):
            cur = cur + [i]
            choose(cur)
            cur = cur[:-1]
        
choose([])

for result in results:
    for j in result:
        print(j, end=" ")
    print()