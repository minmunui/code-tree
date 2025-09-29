from itertools import combinations

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# 오버플로우가 최소로 되는 조합들을 갖춰가는 것이 좋지 않겠나? 모든 경우의 수는 너무 많다.

def get_best():

    candids = []

    def choose(start_idx, cur):
        print(f"choose({start_idx}, {cur})")

        print(f"m : {m}, len(cur) : {len(cur)}, len(nums) : {len(nums)}")
        if sum(map(lambda x : x[1], cur)) >= m:
            print(f"line 28")
            candids.append(cur)
            return

        if len(cur) >= len(nums):
            return

        for i in range(start_idx, len(cur)):
            choose(i + 1, cur + [(i, nums[i])])
            cur = cur[:-1]
    
    choose(0, [])
    return candids

# for mal in range(k):

candids = get_best()
for i in candids:
    print(i)


# for r in range():
# print(combinations(nums))


