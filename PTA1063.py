# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1063 计算谱半径 （20 分）
在数学中，矩阵的“谱半径”是指其特征值的模集合的上确界。换言之，对于给定的 n 个复数空间的特征值 { a1 + b1i , ⋯ , an + bni }，
它们的模为实部与虚部的平方和的开方，而“谱半径”就是最大模。

现在给定一些复数空间的特征值，请你计算并输出这些特征值的谱半径。

输入格式：
输入第一行给出正整数 N（≤ 10 000）是输入的特征值的个数。随后 N 行，每行给出 1 个特征值的实部和虚部，其间以空格分隔。
注意：题目保证实部和虚部均为绝对值不超过 1000 的整数。

输出格式：
在一行中输出谱半径，四舍五入保留小数点后 2 位。

输入样例：

5
0 1
2 0
-1 0
3 3
0 -3

输出样例：

4.24
"""

import math
N = int(input())
max_radius = 0
for i in range(N):
    real, fake = [int(i) for i in input().split()]
    radius = math.sqrt(real**2 + fake**2)
    max_radius = radius if radius > max_radius else max_radius
print('%.2f' % max_radius)
