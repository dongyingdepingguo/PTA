# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1058 选择题 （20 分）
批改多选题是比较麻烦的事情，本题就请你写个程序帮助老师批改多选题，并且指出哪道题错的人最多。

输入格式：
输入在第一行给出两个正整数 N（≤ 1000）和 M（≤ 100），分别是学生人数和多选题的个数。随后 M 行，每行顺次给出一道题的满分值
（不超过 5 的正整数）、选项个数（不少于 2 且不超过 5 的正整数）、正确选项个数（不超过选项个数的正整数）、所有正确选项。
注意每题的选项从小写英文字母 a 开始顺次排列。各项间以 1 个空格分隔。最后 N 行，每行给出一个学生的答题情况，其每题答案格式为
(选中的选项个数 选项1 ……)，按题目顺序给出。注意：题目保证学生的答题情况是合法的，即不存在选中的选项数超过实际选项数的情况。

输出格式：
按照输入的顺序给出每个学生的得分，每个分数占一行。注意判题时只有选择全部正确才能得到该题的分数。最后一行输出错得最多的题目的错误次数和编号
（题目按照输入的顺序从 1 开始编号）。如果有并列，则按编号递增顺序输出。数字间用空格分隔，行首尾不得有多余空格。如果所有题目都没有人错，
则在最后一行输出 Too simple。

输入样例：

3 4
3 4 2 a c
2 5 1 b
5 3 2 b c
1 5 4 a b d e
(2 a c) (2 b d) (2 a c) (3 a b e)
(2 a c) (1 b) (2 a b) (4 a b d e)
(2 b d) (1 e) (2 b c) (4 a b c d)

输出样例：

3
6
5
2 2 3 4

"""

N, M = [int(i) for i in input().split()]
ques_dict = {}
for i in range(1, M+1):
    ques_info = input().split()
    ques_dict[i] = {'score': int(ques_info[0]), 'ans_num': ques_info[2], 'ans': set(ques_info[3:])}

wrong_ans = {}
students_score = []
for j in range(N):
    ans = input().split(') (')
    score = 0
    for k in range(1, M+1):
        an = ans[k-1].lstrip('(').rstrip(')').split()
        if an[0] != ques_dict[k]['ans_num'] or set(an[1:]) != ques_dict[k]['ans']:
            if k not in wrong_ans:
                wrong_ans[k] = 1
            else:
                wrong_ans[k] += 1
            continue
        else:
            score += ques_dict[k]['score']
    students_score.append(score)
for s in students_score:
    print(s)
wrong = sorted(wrong_ans.items(), key=lambda x: (-x[1], x[0]))
times = 0
out = ''
for w in range(len(wrong)):
    if w == 0:
        times = wrong[w][1]
        ques = wrong[w][0]
        out = str(times) + ' ' + str(ques)
    else:
        if wrong[w][1] == times:
            out = out + ' ' + str(wrong[w][0])
        else:
            break
if times == 0:
    out = 'Too simple'
print(out)
