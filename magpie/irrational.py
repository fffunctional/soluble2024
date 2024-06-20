# Given a four digit number ABCD, expand (A + B√C)**D to E + F√C form.

import math

def getDigits(n):
    return [int(x) for x in str(n)]

def expand(n):
    a, b, c, d = getDigits(n)
    currentAddend = a
    currentMultipleOfRoot  = MultipleOfRoot(b, c)
    while d > 1:
        lastAddend = currentAddend
        currentAddend = currentAddend * a + currentMultipleOfRoot * MultipleOfRoot(b, c)
        currentMultipleOfRoot  = MultipleOfRoot(b * lastAddend + a * currentMultipleOfRoot.m, c)
        d = d - 1
    return str(currentAddend) + ' + ' + str(currentMultipleOfRoot)

class MultipleOfRoot:
    def __init__(self, m, r):
        self.m = m
        self.r = r

    def __str__(self):
        return f'{self.m}√{self.r}'

    def __rmul__(self, other):
        return MultipleOfRoot(self.m * other, self.r)

    def __mul__(self, other):
        if isinstance(other, MultipleOfRoot):
            return self.m * other.m * self.r

assert(str(4 * MultipleOfRoot(3, 2)) == str(MultipleOfRoot(12, 2)))
assert(str(MultipleOfRoot(3, 2) * MultipleOfRoot(3, 2)) == '18')
assert(expand(4321) == '4 + ' + str(MultipleOfRoot(3, 2)))
