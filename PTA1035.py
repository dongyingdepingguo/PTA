# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1035 插入与归并 （25 分）
根据维基百科的定义：

插入排序是迭代算法，逐一获得输入数据，逐步产生有序的输出序列。每步迭代中，算法从输入序列中取出一元素，将之插入有序序列中正确的位置。
如此迭代直到全部元素有序。

归并排序进行如下迭代操作：首先将原始序列看成 N 个只包含 1 个元素的有序子序列，然后每次迭代归并两个相邻的有序子序列，
直到最后只剩下 1 个有序的序列。

现给定原始序列和由某排序算法产生的中间序列，请你判断该算法究竟是哪种排序算法？

输入格式：
输入在第一行给出正整数 N (≤100)；随后一行给出原始序列的 N 个整数；最后一行给出由某排序算法产生的中间序列。这里假设排序的目标序列是升序。
数字间以空格分隔。

输出格式：
首先在第 1 行中输出Insertion Sort表示插入排序、或Merge Sort表示归并排序；然后在第 2 行中输出用该排序算法再迭代一轮的结果序列。
题目保证每组测试的结果是唯一的。数字间以空格分隔，且行首尾不得有多余空格。

输入样例 1：

10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

输出样例 1：

Insertion Sort
1 2 3 5 7 8 9 4 6 0

输入样例 2：

10
3 1 2 8 7 5 9 4 0 6
1 3 2 8 5 7 4 9 0 6

输出样例 2：

Merge Sort
1 2 3 8 4 5 7 9 0 6
"""

n = input()
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]


def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    if len(a) > 0:
        result += a
    else:
        result += b
    return result


def merge_sort(L):
    R = []
    L = [[i] for i in L]
    if len(L) <= 1:
        yield L
    while len(L) > 1:
        S = []
        while len(L) > 1:
            a, b = L.pop(0), L.pop(0)
            a_b = merge(a, b)
            S += a_b
            R.append(a_b)
        if L:
            S += L[0]
            R.append(L.pop(0))
        R, L = L, R
        yield S


mer = merge_sort(a)
for i in mer:
    if i == b:
        print('Merge Sort')
        x = next(mer)
        x = [str(i) for i in x]
        print(' '.join(x))
        break


def insert_sort(a):
    if len(a) <= 1:
        yield a
    else:
        for i in range(1, len(a)):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    a[j-1], a[j] = a[j], a[j-1]
                else:
                    break
            yield a


ins = insert_sort(a)
for j in ins:
    if j == b:
        print('Insertion Sort')
        t = next(ins)
        t = [str(j) for j in t]
        print(' '.join(t))
        break
