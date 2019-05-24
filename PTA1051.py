# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1051 复数乘法 （15 分）
复数可以写成 (A+Bi) 的常规形式，其中 A 是实部，B 是虚部，i 是虚数单位，满足 i**2=−1；也可以写成极坐标下的指数形式 (R×e**(Pi))，
其中 R 是复数模，P 是辐角，i 是虚数单位，其等价于三角形式 (R(cos(P)+isin(P))。

现给定两个复数的 R 和 P，要求输出两数乘积的常规形式。

输入格式：
输入在一行中依次给出两个复数的 R​1​, P1, R2 ,P2，数字间以空格分隔。

输出格式：
在一行中按照 A+Bi 的格式输出两数乘积的常规形式，实部和虚部均保留 2 位小数。注意：如果 B 是负数，则应该写成 A-|B|i 的形式。

输入样例：
2.3 3.5 5.2 0.4
输出样例：
-8.68-8.23i
"""

import math
r1, p1, r2, p2 = [float(i) for i in input().split()]
a1 = r1*math.cos(p1)
b1 = r1*math.sin(p1)
a2 = r2*math.cos(p2)
b2 = r2*math.sin(p2)
A = a1*a2 - b1*b2
B = b1*a2 + a1*b2
if -0.05 < A < 0.05 and A != 0:
    A = '0.00'
else:
    A = '%.2f' % A
if -0.05 < B < 0.05 and B != 0:
    B = '+0.00'
else:
    B = '%+.2f' % B
print(A + B + 'i')
