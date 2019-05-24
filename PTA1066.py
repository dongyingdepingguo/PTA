# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1066 图像过滤 （15 分）
图像过滤是把图像中不重要的像素都染成背景色，使得重要部分被凸显出来。现给定一幅黑白图像，要求你将灰度值位于某指定区间内的所有像素颜色
都用一种指定的颜色替换。

输入格式：
输入在第一行给出一幅图像的分辨率，即两个正整数 M 和 N（0<M,N≤500），另外是待过滤的灰度值区间端点 A 和 B（0≤A<B≤255）、
以及指定的替换灰度值。随后 M 行，每行给出 N 个像素点的灰度值，其间以空格分隔。所有灰度值都在 [0, 255] 区间内。

输出格式：
输出按要求过滤后的图像。即输出 M 行，每行 N 个像素灰度值，每个灰度值占 3 位（例如黑色要显示为 000），其间以一个空格分隔。
行首尾不得有多余空格。

输入样例：

3 5 100 150 0
3 189 254 101 119
150 233 151 99 100
88 123 149 0 255

输出样例：

003 189 254 000 000
000 233 151 099 000
088 000 000 000 255
"""

M, N, A, B, grey_value = [int(i) for i in input().split()]
new_image = []
for i in range(M):
    row = input().split()
    for j in range(len(row)):
        if A <= int(row[j]) <= B:
            row[j] = '%03d' % grey_value
        else:
            row[j] = '%03d' % int(row[j])
    new_image.append(row)
for row_image in new_image:
    print(' '.join(row_image))