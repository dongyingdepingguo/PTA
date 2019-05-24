# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1062 最简分数 （20 分）
一个分数一般写成两个整数相除的形式：N/M，其中 M 不为0。最简分数是指分子和分母没有公约数的分数表示形式。

现给定两个不相等的正分数 N1/M1 和 N2/M2，要求你按从小到大的顺序列出它们之间分母为 K 的最简分数。

输入格式：
输入在一行中按 N/M 的格式给出两个正分数，随后是一个正整数分母 K，其间以空格分隔。题目保证给出的所有整数都不超过 1000。

输出格式：
在一行中按 N/M 的格式列出两个给定分数之间分母为 K 的所有最简分数，按从小到大的顺序，其间以 1 个空格分隔。行首尾不得有多余空格。
题目保证至少有 1 个输出。

输入样例：

7/18 13/20 12

输出样例：

5/12 7/12
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def lcm(a, b):
    return int(a*b/gcd(a, b))


NM1, NM2, K = input().split()
N1, M1 = [int(i) for i in NM1.split('/')]
N2, M2 = [int(i) for i in NM2.split('/')]
K = int(K)
L = lcm(lcm(M1, M2), K)
K1 = int(N1*L/M1)
K2 = int(N2*L/M2)
n = []
r = ''
for i in range(1, K):
    if gcd(i, K) == 1 and min(K1, K2) < int(i*L/K) < max(K1, K2):
        n.append('%d/%d'%(i, K))
print(' '.join(n))