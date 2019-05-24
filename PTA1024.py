# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
科学计数法是科学家用来表示很大或很小的数字的一种方便的方法，其满足正则表达式 [+-][1-9].[0-9]+E[+-][0-9]+，即数字的整数部分只有 1 位，
小数部分至少有 1 位，该数字及其指数部分的正负号即使对正数也必定明确给出。

现以科学计数法的格式给出实数 A，请编写程序按普通数字表示法输出 A，并保证所有有效位都被保留。

输入格式：
每个输入包含 1 个测试用例，即一个以科学计数法表示的实数 A。该数字的存储长度不超过 9999 字节，且其指数的绝对值不超过 9999。

输出格式：
对每个测试用例，在一行中按普通数字表示法输出 A，并保证所有有效位都被保留，包括末尾的 0。

输入样例 1：
+1.23400E-03

输出样例 1：
0.00123400

输入样例 2：
-1.2E+10

输出样例 2：
-12000000000
"""

import re

N = input()
match = re.search(r"[+-][1-9]\.[0-9]+E[+-][0-9]+", N)

if match != None:
    N1 = N.split('E')
    polar_value = N1[0]
    index_value = int(N1[1])
    if abs(index_value) > 9999:
        exit(0)
    polar_list = list(polar_value)
    if index_value <= 0:
        for i in range(abs(index_value)):
            polar_list.insert(i+1, '0')
        polar_list.insert(2, polar_list.pop(polar_list.index('.')))
    else:
        if len(polar_list) <= index_value +3:
            cur = index_value - len(polar_list) + 3
            for j in range(cur):
                polar_list.append('0')
            polar_list.remove('.')
        else:
            polar_list.insert(index_value + 2, polar_list.pop(polar_list.index('.')))
    if polar_list[0] == '+':
        polar_list.remove('+')
    polar_str = ''.join(polar_list)
    print(polar_str)
