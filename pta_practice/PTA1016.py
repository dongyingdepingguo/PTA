
# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
正整数 A 的“DA（为 1 位整数）部分”定义为由 A 中所有 D​A 组成的新整数 PA。例如：给定 A=3862767，DA=6，则 A 的“6 部分”PA是 66，
因为 A 中有 2 个 6。

现给定 A、D​A、B、DB，请编写程序计算 PA + PB。

输入格式：
输入在一行中依次给出 A、D​A、B、DB，中间以空格分隔，其中 0<A,B<10e​10。

输出格式：
在一行中输出 PA + P​B 的值。

输入样例 1：
3862767 6 13530293 3

输出样例 1：
399

输入样例 2：
3862767 1 13530293 8

输出样例 2：
0
"""

initial_list = input().split(' ')
DN = []
for i in range(len(initial_list)//2):
    count_D = 0
    for D in initial_list[2*i]:
        if D == initial_list[2*i+1]:
            count_D += 1
            part = int(D * count_D)
    if count_D == 0:
        part = 0
    DN.append(part)
res = 0
for j in DN:
    res = j + res
print(res)