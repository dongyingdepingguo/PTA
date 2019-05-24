# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1048 数字加密 （20 分）
本题要求实现一种数字加密方法。首先固定一个加密用正整数 A，对任一正整数 B，将其每 1 位数字与 A 的对应位置上的数字进行以下运算：对奇数位，
对应位的数字相加后对 13 取余——这里用 J 代表 10、Q 代表 11、K 代表 12；对偶数位，用 B 的数字减去 A 的数字，若结果为负数，则再加 10。
这里令个位为第 1 位。

输入格式：
输入在一行中依次给出 A 和 B，均为不超过 100 位的正整数，其间以空格分隔。

输出格式：
在一行中输出加密后的结果。

输入样例：

1234567 368782971

输出样例：

3695Q8118
"""

A, B = input().split()
re_d = {10: 'J', 11: 'Q', 12: 'K'}
result = ''
n = len(A) if len(A) > len(B) else len(B)
if len(A) - len(B) > 0:
    B = (len(A) - len(B))*'0' + B
else:
    A = (len(B) - len(A))*'0' + A
for i in range(1,len(A)+1):
    if i % 2 != 0:
        re = (int(B[len(A)-i]) + int(A[len(A)-i])) % 13
        if re >= 10:
            re = re_d[re]
    else:
        re = int(B[len(A)-i]) - int(A[len(A)-i])
        if re < 0:
            re = re + 10
    result = str(re) + result
print(result)