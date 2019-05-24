# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
1032 挖掘机技术哪家强 （20 分）
为了用事实说明挖掘机技术到底哪家强，PAT 组织了一场挖掘机技能大赛。现请你根据比赛结果统计出技术最强的那个学校。

输入格式：
输入在第 1 行给出不超过10**​5 的正整数 N，即参赛人数。随后 N 行，每行给出一位参赛者的信息和成绩，
包括其所代表的学校的编号（从 1 开始连续编号）、及其比赛成绩（百分制），中间以空格分隔。

输出格式：
在一行中给出总得分最高的学校的编号、及其总分，中间以空格分隔。题目保证答案唯一，没有并列。

输入样例：
6
3 65
2 80
1 100
2 70
3 40
3 0
输出样例：
2 150
"""

# 测试超时

n = int(input())
info_dict = {}
max_core = 0
max_item = None
for i in range(n):
    info = input().split()
    if info[0] not in info_dict:
        info_dict[info[0]] = int(info[1])
    else:
        info_dict[info[0]] += int(info[1])

for item in info_dict:
    if info_dict[item] > max_core:
        max_core = info_dict[item]
        max_item = item
# max_item = sorted(info_dict.items(), key=lambda x: x[1])[-1]
print(str(max_item)+' '+str(max_core))
