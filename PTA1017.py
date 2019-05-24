# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
本题要求计算 A/B，其中 A 是不超过 1000 位的正整数，B 是 1 位正整数。你需要输出商数 Q 和余数 R，使得 A=B×Q+R 成立。

输入格式：
输入在一行中依次给出 A 和 B，中间以 1 空格分隔。

输出格式：
在一行中依次输出 Q 和 R，中间以 1 空格分隔。

输入样例：
123456789050987654321 7

输出样例：
17636684150141093474 3
"""

A, B = input().split(' ')
Y = 0
P_res = []
for i in A:
    m = Y * 10 + int(i)
    P = m // int(B)
    Y = m % int(B)
    P_res.append(P)
P_res_pro = ''.join([str(i) for i in P_res]).lstrip('0')
print(' '.join([P_res_pro, str(Y)]))
