# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
一个数组A中存有N（>0）个整数，在不允许使用另外数组的前提下，将每个整数循环向右移M（≥0）个位置，即将A中的数据由（A​0A1 ⋯ A(N−1)）变换为
（A(N−M) ​​⋯ A(N−1)A0A1 ⋯ A(N−M−1)）（最后M个数循环移至最前面的M个位置）。如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？

输入格式:
每个输入包含一个测试用例，第1行输入N（1≤N≤100）和M（≥0）；第2行输入N个整数，之间用空格分隔。

输出格式:
在一行中输出循环右移M位以后的整数序列，之间用空格分隔，序列结尾不能有多余空格。

输入样例:
6 2
1 2 3 4 5 6

输出样例:
5 6 1 2 3 4
"""

L = input().split(' ')
N = int(L[0])
M = int(L[1])
input_list = input().split(' ')
for i in range(M):
    input_list.insert(0, input_list.pop())
print(' '.join(input_list))
