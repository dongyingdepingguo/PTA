# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
设计函数求一元多项式的导数。

输入格式:
以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过 1000 的整数）。数字间以空格分隔。

输出格式:
以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格。注意“零多项式”的指数和系数都是 0，但是表示为 0
0。

输入样例:
3 4 -5 2 6 1 -2 0
输出样例:
12 3 -10 1 6 0
"""

derivation_list = [int(i) for i in input().split(' ')]
derivated_list = []

if len(derivation_list) == 2 and derivation_list[1] == 0:
    derivated_list.extend(['0','0'])

else:
    terms_number = int(len(derivation_list) / 2)
    for n in range(terms_number):
        coefficient = derivation_list[2*n] * derivation_list[2*n + 1]
        if coefficient == 0:
            continue
        else:
            derivated_list.append(str(coefficient))
            index = derivation_list[2*n+1] - 1
            derivated_list.append(str(index))
print(' '.join(derivated_list))
