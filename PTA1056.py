# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1056 组合数的和 （15 分）
给定 N 个非 0 的个位数字，用其中任意 2 个数字都可以组合成 1 个 2 位的数字。要求所有可能组合出来的 2 位数字的和。例如给定 2、5、8，则可以组合出：25、28、52、58、82、85，它们的和为330。

输入格式：
输入在第一行中给出 N（1 < N < 10），随后一行给出 N 个不同的非 0 个位数字。数字间以空格分隔。

输出格式：
输出所有可能组合出来的2位数字的和。

输入样例：

3
2 8 5

输出样例：

330
"""

a = [int(i) for i in input().split()]
N, basic_unit = a[0], a[1:]
result = 0
for i in range(N):
    for j in range(i+1, N):
        result = result + basic_unit[i]*10+basic_unit[j] + basic_unit[j]*10 + basic_unit[i]
print(result)
