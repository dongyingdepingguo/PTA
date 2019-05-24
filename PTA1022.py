# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
输入两个非负 10 进制整数 A 和 B (≤2e30 −1)，输出 A+B 的 D (1<D≤10)进制数。

输入格式：
输入在一行中依次给出 3 个整数 A、B 和 D。

输出格式：
输出 A+B 的 D 进制数。

输入样例：
123 456 8

输出样例：
1103
"""

N1 = [int(i) for i in input().split(' ')]


def f(N):
    if N[2] > 10 or N[2] <= 1:
        exit()
    E = []
    C = N[0] + N[1]
    while C > 0:
        Y = C % N[2]
        C = C // N[2]
        E.append(str(Y))
    E.reverse()
    return ''.join(E)
print(f(N1))