# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1047 编程团体赛 （20 分）
编程团体赛的规则为：每个参赛队由若干队员组成；所有队员独立比赛；参赛队的成绩为所有队员的成绩和；成绩最高的队获胜。

现给定所有队员的比赛成绩，请你编写程序找出冠军队。

输入格式：
输入第一行给出一个正整数 N（≤10**​4），即所有参赛队员总数。随后 N 行，每行给出一位队员的成绩，格式为：队伍编号-队员编号 成绩，
其中队伍编号为 1 到 1000 的正整数，队员编号为 1 到 10 的正整数，成绩为 0 到 100 的整数。

输出格式：
在一行中输出冠军队的编号和总成绩，其间以一个空格分隔。注意：题目保证冠军队是唯一的。

输入样例：

6
3-10 99
11-5 87
102-1 0
102-3 100
11-9 89
3-2 61

输出样例：

11 176
"""

n = int(input())
teams_info = []
teams_score = {}
for i in range(n):
    team_info, score = input().split()
    team_number, member_number = team_info.split('-')
    teams_info.append([team_number, member_number, int(score)])
for t_i in teams_info:
    if t_i[0] not in teams_score:
        teams_score[t_i[0]] = t_i[2]
    else:
        teams_score[t_i[0]] += t_i[2]
re = sorted(teams_score.items(), key=lambda x: x[1], reverse=True)
print(re[0][0]+' '+str(re[0][1]))
