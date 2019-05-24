# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1059 C语言竞赛 （20 分）
C 语言竞赛是浙江大学计算机学院主持的一个欢乐的竞赛。既然竞赛主旨是为了好玩，颁奖规则也就制定得很滑稽：

0、冠军将赢得一份“神秘大奖”（比如很巨大的一本学生研究论文集……）。
1、排名为素数的学生将赢得最好的奖品 —— 小黄人玩偶！
2、其他人将得到巧克力。
给定比赛的最终排名以及一系列参赛者的 ID，你要给出这些参赛者应该获得的奖品。

输入格式：
输入第一行给出一个正整数 N（≤10
​4
​​ ），是参赛者人数。随后 N 行给出最终排名，每行按排名顺序给出一位参赛者的 ID（4 位数字组成）。接下来给出一个正整数 K 以及 K个需要查询的ID。

输出格式：
对每个要查询的 ID，在一行中输出 ID: 奖品，其中奖品或者是 Mystery Award（神秘大奖）、或者是 Minion（小黄人、或者是Chocolate（巧克力）。
如果所查 ID 根本不在排名里，打印 Are you kidding?（耍我呢？）。如果该 ID 已经查过了（即奖品已经领过了），
打印 ID: Checked（不能多吃多占）。

输入样例：

6
1111
6666
8888
1234
5555
0001
6
8888
0001
1111
2222
8888
2222

输出样例：

8888: Minion
0001: Chocolate
1111: Mystery Award
2222: Are you kidding?
8888: Checked
2222: Are you kidding?
"""

import math
N = int(input())
partci_rank = {}
for i in range(1, N+1):
    ID = input()
    if i == 1:
        partci_rank[ID] = {'award': 'Mystery Award', 'state': 0}
    else:
        rem = -1
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0 and i != j:
                rem = 0
                break
        if rem == 0:
            partci_rank[ID] = {'award': 'Chocolate', 'state': 0}
        else:
            partci_rank[ID] = {'award': 'Minion', 'state': 0}
K = int(input())
Check_ID = []
for k in range(K):
    Check_ID.append(input())
for ID_num in Check_ID:
    try:
        award = partci_rank[ID_num]['award']
        state = partci_rank[ID_num]['state']
    except KeyError:
        print(ID_num + ': ' + 'Are you kidding?')
    else:
        if state == 0:
            print(ID_num + ': ' + award)
            partci_rank[ID_num]['state'] = 1
        else:
            print(ID_num + ': ' + 'Checked')