# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
令 P​i 表示第 i 个素数。现任给两个正整数 M≤N≤10e4，请输出 P​M 到 PN 的所有素数。

输入格式：
输入在一行中给出 M 和 N，其间以空格分隔。

输出格式：
输出从 P​M 到 PN 的所有素数，每 10 个数字占 1 行，其间以空格分隔，但行末不得有多余空格。

输入样例：
5 27

输出样例：
11 13 17 19 23 29 31 37 41 43
47 53 59 61 67 71 73 79 83 89
97 101 103
"""


def int_creator():
    i = 2
    while True:
        yield i
        i += 1


def even_filter(n):
    return lambda x: x % n != 0


def p_creator(k):
    it = int_creator()
    i = 0
    while i < k:
        i += 1
        n = next(it)
        yield n
        it = filter(even_filter(n), it)


P = [int(i) for i in input().split(' ')]
p_number = [str(j) for j in p_creator(P[1])][P[0] - 1:]
p_split_num = [p_number[k:k + 10] for k in range(0, len(p_number), 10)]
for p_split in p_split_num:
    print(' '.join(p_split))