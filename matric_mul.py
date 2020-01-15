from numpy import *

m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('11 12 13 ; 14 15 16 ; 17 18 19')

print("matrix mul using inbuilt \n {}".format(m1 * m2))
a, b = m1.shape
c, d = m2.shape
if b == c:
    m3 = empty(shape=(a, d), dtype=int)

for i in range(a):
    for k in range(d):
        sum = 0
        for j in range(d):
            sum += m1[i, j] * m2[j, k]

        m3[i, k] = sum

print("matrix mul done using for \n {}".format(m3))

