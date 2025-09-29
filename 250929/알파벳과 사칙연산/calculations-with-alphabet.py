expression = input()

# Please write your code here.
opers = ["+", "-", "*"]
chars = ["a", "b", "c", "d", "e", "f"]

result = 0
last = None

for i, cur in enumerate(expression):
    if i == 0:
        result = 4
    
    elif cur in opers:
        last = cur

    elif cur in chars:
        if last == "+":
            result += 4
        if last == "-":
            result -= 1
        if last == "*":
            if result < 0:
                result *= 1
            else:
                result *= 4

print(result)