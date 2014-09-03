import math

for x in xrange(1,16):
    print x, math.pow(2, math.floor(math.log(x,2))) -1


def foo():
    array = [True, True, False]
    for value in array:
        if not value:
            return False

a = foo()
print a
