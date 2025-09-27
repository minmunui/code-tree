from itertools import combinations

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

edges = sorted(edges, key=lambda x : x[1])
# print(edges) 

# Please write your code here.
def get_ladder_output(n_cols, edges):
    edges = sorted(edges, key=lambda x : x[1])
    result = list(range(n_cols))
    for edge in edges:
        idx = edge[0] - 1
        result[idx], result[idx + 1] = result[idx + 1], result[idx]
    return result
    
target = get_ladder_output(n, edges)

def main():
    for i in range(0, len(edges) + 1):
        cases = combinations(edges, i)
        for _case in cases:
            if get_ladder_output(n, _case) == target:
                print(len(_case))
                return

main()