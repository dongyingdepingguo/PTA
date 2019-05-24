# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1054 求平均值 （20 分）
本题的基本要求非常简单：给定 N 个实数，计算它们的平均值。但复杂的是有些输入数据可能是非法的。
一个“合法”的输入是 [−1000,1000] 区间内的实数，并且最多精确到小数点后 2 位。当你计算平均值的时候，不能把那些非法的数据算在内。

输入格式：
输入第一行给出正整数 N（≤100）。随后一行给出 N 个实数，数字间以一个空格分隔。

输出格式：
对每个非法输入，在一行中输出 ERROR: X is not a legal number，其中 X 是输入。最后在一行中输出结果：The average of K numbers is Y，
其中 K 是合法输入的个数，Y 是它们的平均值，精确到小数点后 2 位。如果平均值无法计算，则用 Undefined 替换 Y。如果 K 为 1，
则输出 The average of 1 number is Y。

输入样例 1：

7
5 -3.2 aaa 9999 2.3.4 7.123 2.35

输出样例 1：

ERROR: aaa is not a legal number
ERROR: 9999 is not a legal number
ERROR: 2.3.4 is not a legal number
ERROR: 7.123 is not a legal number
The average of 3 numbers is 1.38

输入样例 2：

2
aaa -9999

输出样例 2：

ERROR: aaa is not a legal number
ERROR: -9999 is not a legal number
The average of 0 numbers is Undefined
"""

N = input()
numbers = input().split()
total, count = 0, 0
for number in numbers:
    try:
        float_number = float(number)
    except ValueError:
        print('ERROR: %s is not a legal number' % number)
    else:
        if float_number < -1000 or float_number > 1000:
            print('ERROR: %s is not a legal number' % number)
        else:
            _, dot_after = str(float_number).split('.')
            if len(dot_after) > 2:
                print('ERROR: %s is not a legal number' % number)
            else:
                total += float_number
                count += 1
if count == 0:
    print('The average of 0 numbers is Undefined')
elif count == 1:
    print('The average of %d number is %.2f' % (count, total))
else:
    print('The average of %d numbers is %.2f' % (count, total/count))