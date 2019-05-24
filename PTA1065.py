# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1065 单身狗 （25 分）
“单身狗”是中文对于单身人士的一种爱称。本题请你从上万人的大型派对中找出落单的客人，以便给予特殊关爱。

输入格式：
输入第一行给出一个正整数 N（≤ 50 000），是已知夫妻/伴侣的对数；随后 N 行，每行给出一对夫妻/伴侣——为方便起见，每人对应一个 ID 号，
为 5 位数字（从 00000 到 99999），ID 间以空格分隔；之后给出一个正整数 M（≤ 10 000），为参加派对的总人数；随后一行给出这 M 位客人的 ID，
以空格分隔。题目保证无人重婚或脚踩两条船。

输出格式：
首先第一行输出落单客人的总人数；随后第二行按 ID 递增顺序列出落单的客人。ID 间用 1 个空格分隔，行的首尾不得有多余空格。

输入样例：

3
11111 22222
33333 44444
55555 66666
7
55555 44444 10000 88888 22222 11111 23333

输出样例：

5
10000 23333 44444 55555 88888
"""

N = int(input())
couple_dict = {}
for i in range(N):
    m, w = input().split()
    couple_dict[m] = w
M = int(input())
party_number = input().split()
party_set = set(party_number)  # 此处把列表改为集合，查询速度会快一些
for j in party_number[::]:
    if j in couple_dict and couple_dict[j] in party_set:
        party_number.remove(j)
        party_number.remove(couple_dict[j])
party_single = sorted(party_number)
num = len(party_single)
print(num)
if num != 0:
    print(' '.join(party_single))
