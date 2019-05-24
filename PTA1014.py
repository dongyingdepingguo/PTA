# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
大侦探福尔摩斯接到一张奇怪的字条：我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm。大侦探很快就明白了，字条上奇
怪的乱码实际上就是约会的时间星期四 14:04，因为前面两字符串中第 1 对相同的大写英文字母（大小写有区分）是第 4 个字母 D，代表星期四；第 2 对
相同的字符是 E ，那是第 5 个英文字母，代表一天里的第 14 个钟头（于是一天的 0 点到 23 点由数字 0 到 9、以及大写字母 A 到 N 表示）；后面
两字符串第 1 对相同的英文字母 s 出现在第 4 个位置（从 0 开始计数）上，代表第 4 分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。

输入格式：
输入在 4 行中分别给出 4 个非空、不包含空格、且长度不超过 60 的字符串。

输出格式：
在一行中输出约会的时间，格式为 DAY HH:MM，其中 DAY 是某星期的 3 字符缩写，即 MON 表示星期一，TUE 表示星期二，WED 表示星期三，THU 表示
星期四，FRI 表示星期五，SAT 表示星期六，SUN 表示星期日。题目输入保证每个测试存在唯一解。

输入样例：
3485djDkxh4hhGE
2984akDfkkkkggEdsb
s&hgsfdk
d&Hyscvnm

输出样例：
THU 14:04
"""

secret = []
DAY = {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 7: 'SUN'}
for i in range(4):
    secret.append(input())
for j in range(min(len(secret[0]),len(secret[1]))):
    if secret[0][j] == secret[1][j] and 'A' <= secret[0][j] <= 'G':
        DAY = DAY[ord(secret[0][j])-64]
        n = j
        break
for i in range(n+1, min(len(secret[0]),len(secret[1]))):
    if secret[0][i] == secret[1][i]:
        if '0' <= secret[0][i] <= '9':
            HH = ord(secret[0][i]) - 48
        elif 'A' <= secret[0][i] <= 'N':
            HH = ord(secret[0][i]) - 55
        else:
            continue
        HH = '%02d'%HH
        break

for k in range(min(len(secret[2]), len(secret[3]))):
    if secret[2][k] == secret[3][k]:
        if 'a' <= secret[2][k] <= 'z' or 'A' <= secret[2][k] <= 'Z':
            MM = '%02d' % k
            break

print(DAY+' '+HH+':'+MM)