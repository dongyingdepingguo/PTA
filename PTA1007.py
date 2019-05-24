# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
让我们定义d​n为：d​n = p(n+1) − pn，其中 pi 是第i个素数。显然有 d1=1，且对于n>1有dn是偶数。“素数对猜想”认为“存在无穷多对相邻且差为
2的素数”。

现给定任意正整数N(<10e5)，请计算不超过N的满足猜想的素数对的个数。

输入格式:
输入在一行给出正整数N。

输出格式:
在一行中输出不超过N的满足猜想的素数对的个数。

输入样例:
20

输出样例:
4
"""

import math


def prime_number(N):
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True


n = int(input())
count = 0
for j in range(2,n+1):
    if prime_number(j) and prime_number(j+2):
        count += 1
print(count)
