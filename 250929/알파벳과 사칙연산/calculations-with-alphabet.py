combs = []
chars = ["a", "b", "c", "d", "e", "f"]
opers = ["+", "-", "*"]

def choose(cur, n, r):

    if len(cur) >= r:
        # print(f"cur : {cur}, r : {r}")
        combs.append(cur)
        return
    
    else:
        for i in n:
            cur = cur + [i]
            choose(cur, n, r)
            cur = cur[:-1]

choose([], [1, 2, 3, 4], len(chars))

# print(combs)

expression = input()

def get_value(exp, values):
    dict_value = {
        "a" : values[0],
        "b" : values[1],
        "c" : values[2],
        "d" : values[3],
        "e" : values[4],
        "f" : values[5],
    }
    last = None
    result = -(2 ** 31)
    for i, char in enumerate(exp):
        # print(f"char = {char}, result = {result}, ", end = "")
        if i == 0:
            result = dict_value[char]
        elif char in chars:
            if last == "+":
                result += int(dict_value[char])
            elif last == "-":
                result -= int(dict_value[char])
            elif last == "*":
                result *= int(dict_value[char])
        elif char in opers:
            last = char
        # print(f"after_result = {result}")
    return result


maxima = -(2 ** 32)
arr = []
for comb in combs:
    # print(f"comb : {comb}")
    value = get_value(expression, comb)
    # print(f"value : {value}")
    if value > maxima:
        maxima = value
        arr = comb

print(maxima)
# print(arr)