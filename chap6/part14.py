def adder(n):
    return lambda total: total + n

smalladder = adder(5)

result = smalladder(10)

print(result)
