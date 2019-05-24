# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1030 完美数列
给定一个正整数数列，和正整数 p，设这个数列中的最大值是 M，最小值是 m，如果 M≤mp，则称这个数列是完美数列。

现在给定参数 p 和一些正整数，请你从中选择尽可能多的数构成一个完美数列。

输入格式：
输入第一行给出两个正整数 N 和 p，其中 N（≤10**5）是输入的正整数的个数，p（≤10**9）是给定的参数。第二行给出 N 个正整数，
每个数不超过 10​**9。

输出格式：
在一行中输出最多可以选择多少个数可以用它们组成一个完美数列。

输入样例：
10 8
2 3 20 4 5 1 6 7 8 9
输出样例：
8
"""

# 我的方法，时间上没通过
from copy import deepcopy
a, n = [int(i) for i in input().split()]
original_list = [int(i) for i in input().split()]
max_number_list = []
for index, i in enumerate(sorted(deepcopy(original_list))):
    b = deepcopy(original_list)
    c = i * n
    b.append(c)
    b = sorted(b)
    c_number = b.count(c)
    c_index = b.index(c)
    if c_number > 1:
        max_number = c_index - index + c_number - 1
    else:
        max_number = c_index - index
    max_number_list.append(max_number)
print(max(max_number_list))

# 网上神仙的做法
number, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)
max_num = 0
for index, i in enumerate(a):
    max_a = i * n
    for j in range(index+max_num, number):
        if a[j] <= max_a:
            max_num += 1
        else:
            break
print(max_num)
