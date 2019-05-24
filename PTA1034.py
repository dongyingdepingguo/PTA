# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1034 有理数四则运算 （20 分）
本题要求编写程序，计算 2 个有理数的和、差、积、商。

输入格式：
输入在一行中按照 a1/b1 a2/b2 的格式给出两个分数形式的有理数，其中分子和分母全是整型范围内的整数，负号只可能出现在分子前，分母不为 0。

输出格式：
分别在 4 行中按照 有理数1 运算符 有理数2 = 结果 的格式顺序输出 2 个有理数的和、差、积、商。
注意输出的每个有理数必须是该有理数的最简形式 k a/b，其中 k 是整数部分，a/b 是最简分数部分；若为负数，则须加括号；若除法分母为 0，
则输出 Inf。题目保证正确的输出中没有超过整型范围的整数。

输入样例1：

2/3 -4/2

输出样例 1：

2/3 + (-2) = (-1 1/3)
2/3 - (-2) = 2 2/3
2/3 * (-2) = (-1 1/3)
2/3 / (-2) = (-1/3)

输入样例2：

5/3 0/6

输出样例 2：

1 2/3 + 0 = 1 2/3
1 2/3 - 0 = 1 2/3
1 2/3 * 0 = 0
1 2/3 / 0 = Inf
"""

input_content = input().split()
a1, b1 = [int(i) for i in input_content[0].split('/')]
a2, b2 = [int(i) for i in input_content[1].split('/')]
a = [a1, a2]
b = [b1, b2]


def common_divisor(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        b, a = a % b, b
    return a


def simplify_number(A, B):
    n = common_divisor(abs(A), abs(B))
    A = int(A / n)
    B = int(B / n)
    if B < 0:
        A = -A
        B = -B
    k = int(A / B)
    a = abs(A) % B
    if A < 0:
        if a == 0:
            out = '(%d)' % k
        else:
            if k == 0:
                out = '(%d/%d)' % (A, B)
            else:
                out = '(%d %d/%d)' % (k, a, B)
    else:
        if a == 0:
            out = '%d' % k
        else:
            if k == 0:
                out = '%d/%d' % (A, B)
            else:
                out = '%d %d/%d' % (k, a, B)
    return out


a_out = simplify_number(a[0], b[0])
b_out = simplify_number(a[1], b[1])


def s(a, b):
    A = a[0] * b[1] + a[1] * b[0]
    B = b[0] * b[1]
    return '%s + %s = %s'%(a_out, b_out, simplify_number(A, B))


def d(a, b):
    A = a[0] * b[1] - a[1] * b[0]
    B = b[0] * b[1]
    return '%s - %s = %s' % (a_out, b_out, simplify_number(A, B))


def m(a, b):
    A = a[0] * a[1]
    B = b[0] * b[1]
    return '%s * %s = %s' % (a_out, b_out, simplify_number(A, B))


def dv(a, b):
    A = a[0] * b[1]
    B = b[0] * a[1]
    if B == 0:
        return '%s / %s = %s' % (a_out, b_out, 'Inf')
    else:
        return '%s / %s = %s' % (a_out, b_out, simplify_number(A, B))


print(s(a, b), d(a, b), m(a, b), dv(a, b), sep='\n')
