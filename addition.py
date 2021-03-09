nums = [1, 2, 3, 4, 5]   # list of integers
_sum = 0   # initial sum of integers


# if there is any variable assigment inside the
# `add` function then python will treat that
# variable as locally scoped but since global
# keyword is specified it will actually use the
# globally scoped variable `_sum`
def add(n):
    global _sum
    _sum += n
    return _sum


result = list(map(add, nums))
# printing the sum
print(f"The sum of {nums} is {result[-1]} or {_sum}.")
