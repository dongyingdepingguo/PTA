# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1053 住房空置率 （20 分）
在不打扰居民的前提下，统计住房空置率的一种方法是根据每户用电量的连续变化规律进行判断。判断方法如下：

在观察期内，若存在超过一半的日子用电量低于某给定的阈值 e，则该住房为“可能空置”；

若观察期超过某给定阈值 D 天，且满足上一个条件，则该住房为“空置”。

现给定某居民区的住户用电量数据，请你统计“可能空置”的比率和“空置”比率，即以上两种状态的住房占居民区住房总套数的百分比。

输入格式：
输入第一行给出正整数 N（≤1000），为居民区住房总套数；正实数 e，即低电量阈值；正整数 D，即观察期阈值。随后 N 行，
每行按以下格式给出一套住房的用电量数据：

K E​1 E2​​  ... EK​​

其中 K 为观察的天数，Ei为第 i 天的用电量。

输出格式：
在一行中输出“可能空置”的比率和“空置”比率的百分比值，其间以一个空格分隔，保留小数点后 1 位。

输入样例：

5 0.5 10
6 0.3 0.4 0.5 0.2 0.8 0.6
10 0.0 0.1 0.2 0.3 0.0 0.8 0.6 0.7 0.0 0.5
5 0.4 0.3 0.5 0.1 0.7
11 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1
11 2 2 2 1 1 0.1 1 0.1 0.1 0.1 0.1

输出样例：

40.0% 20.0%
"""

N, e, D = [float(i) for i in input().split()]
house_info_list = []
for n in range(int(N)):
    house_info_list.append([float(i) for i in input().split()])
unoccupied, may_unoccupied = 0, 0
for house_info in house_info_list:
    check_time, power_qu = house_info[0], house_info[1:]
    count = 0
    for i in power_qu:
        if i < e:
            count += 1
    if count > check_time/2 and check_time <= D:
        may_unoccupied += 1
    if count > check_time/2 and check_time > D:
        unoccupied += 1
print('%.1f%% %.1f%%' % (may_unoccupied*100/N, unoccupied*100/N))
