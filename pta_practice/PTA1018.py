# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
大家应该都会玩“锤子剪刀布”的游戏，现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。

输入格式：
输入第 1 行给出正整数 N（≤10e5），即双方交锋的次数。随后 N 行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。C 代表“锤子”、
J 代表“剪刀”、B 代表“布”，第 1 个字母代表甲方，第 2 个代表乙方，中间有 1 个空格。

输出格式：
输出第 1、2 行分别给出甲、乙的胜、平、负次数，数字间以 1 个空格分隔。第 3 行给出两个字母，分别代表甲、乙获胜次数最多的手势，
中间有 1 个空格。如果解不唯一，则输出按字母序最小的解。

输入样例：
10
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J

输出样例：
5 3 2
2 3 5
B B
"""

A_V = (['C', 'J'], ['J', 'B'], ['B', 'C'])
V_V = (['C', 'C'], ['J', 'J'], ['B', 'B'])
A_V_count, V_V_count, B_V_count = 0, 0, 0
A_num = {'C': 0, 'J': 0, 'B': 0}
B_num = {'C': 0, 'J': 0, 'B': 0}
times = int(input())
for i in range(times):
    battle = input().split()
    if battle in A_V:
        A_V_count += 1
        A_num[battle[0]] += 1
    elif battle in V_V:
        V_V_count += 1
    else:
        B_V_count += 1
        B_num[battle[1]] += 1
print(A_num, B_num)
print(' '.join([str(i) for i in [A_V_count, V_V_count, B_V_count]]))
print(' '.join([str(i) for i in [B_V_count, V_V_count, A_V_count]]))
print(' '.join([sorted(A_num.items(), key=lambda x:(-x[1], x[0]))[0][0],
                sorted(B_num.items(), key=lambda x:(-x[1], x[0]))[0][0]]))