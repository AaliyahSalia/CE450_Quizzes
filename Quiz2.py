from math import sqrt
def  is_sqrt(seq):
    return [x for x in seq if sqrt(x) == int(sqrt(x))]

seq = [49, 8, 2, 1, 102]
print(is_sqrt(seq))
seq = [500, 30]
print(is_sqrt(seq))

