# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1050 螺旋矩阵 （25 分）
本题要求将给定的 N 个正整数按非递增的顺序，填入“螺旋矩阵”。所谓“螺旋矩阵”，是指从左上角第 1 个格子开始，按顺时针螺旋方向填充。
要求矩阵的规模为 m 行 n 列，满足条件：m×n 等于 N；m≥n；且 m−n 取所有可能值中的最小值。

输入格式：
输入在第 1 行中给出一个正整数 N，第 2 行给出 N 个待填充的正整数。所有数字不超过 10**4，相邻数字以空格分隔。

输出格式：
输出螺旋矩阵。每行 n 个数字，共 m 行。相邻数字以 1 个空格分隔，行末不得有多余空格。

输入样例：

12
37 76 20 98 76 42 53 95 60 81 58 93

输出样例：

98 95 93
42 37 81
53 20 76
58 60 76

"""

N = int(input())
original_list = [int(i) for i in input().split()]
ordered_list = sorted(original_list, reverse=True)


def get_row_cloumn(N):
    import math
    n = int(math.sqrt(N))
    remainder = -1
    while n>0 and remainder != 0:
        remainder = N % n
        n -= 1
    return int(N/(n+1)), n+1


def get_zero_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix.append([0]*n)
    return matrix


def get_spiral_coordinate(m_min, m_max, n_min, n_max):
    i, j = 0, 0
    count = 1
    while n_min != int((n_max+n_min)/2) + 1:
        if count % 2 != 0:
            while j <= n_max:
                j += 1
                yield i, j-1
            j = j - 1
            m_min += 1
            i = m_min
            while i <= m_max:
                i += 1
                yield i-1, j
            i = i -1
            n_max -= 1
            count += 1
        else:
            while j > n_min:
                j -= 1
                yield i, j
            m_max -= 1
            while i > m_min:
                i -= 1
                yield i, j
            j += 1
            n_min += 1
            count += 1


m, n = get_row_cloumn(N)
zero_matrix = get_zero_matrix(m, n)
spiral_coordinate = get_spiral_coordinate(0, m-1, 0, n-1)
for number in ordered_list:
    i, j = next(spiral_coordinate)
    zero_matrix[i][j] = str(number)
for i in zero_matrix:
    print(' '.join(i))
