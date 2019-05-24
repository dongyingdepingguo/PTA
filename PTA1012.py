# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：

A​1 = 能被 5 整除的数字中所有偶数的和；
A2 = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 n​1 − n2 + n3 − n4 ⋯；
A3 = 被 5 除后余 2 的数字的个数；
A4 = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
A5 = 被 5 除后余 4 的数字中最大数字。

输入格式：
每个输入包含 1 个测试用例。每个测试用例先给出一个不超过 1000 的正整数 N，随后给出 N 个不超过 1000 的待分类的正整数。数字间以空格分隔。

输出格式：
对给定的 N 个正整数，按题目要求计算 A1 ~ A5 并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。

若其中某一类数字不存在，则在相应位置输出 N。

输入样例 1：
13 1 2 3 4 5 6 7 8 9 10 20 16 18

输出样例 1：
30 11 2 9.7 9

输入样例 2：
8 1 2 4 5 6 7 9 16

输出样例 2：
N 11 2 N 9
"""

number_list = [int(i) for i in input().split(' ')]
category_list = []
A1 = 0
A2 = 0
A3 = 0
a4 = 0
A5 = 0
count_a2 = 0
count_a4 = 0
for j in number_list:
    if j % 2 == 0:
        if j % 5 == 0:
            A1 = A1 + j
    elif j % 5 == 1:
        count_a2 += 1
        A2 = A2 + (-1)**(count_a2+1) * j
    elif j % 5 == 2:
        A3 += 1
    elif j % 5 == 3:
        count_a4 += 1
        a4 = a4 + j
    elif j % 5 == 4:
        if j > A5:
            A5 = j
A4 = round(a4/count_a4, 1)
for n in [str(n) for n in [A1, A2, A3, A4, A5]]:
    if n == '0':
        n = 'N'
    category_list.append(n)
print(' '.join(category_list))