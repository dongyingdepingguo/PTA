# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""

"""
hands, eyes, mouth = [], [], []
n_list = []
for j in [hands, eyes, mouth]:
    expression = input()
    expression = (i for i in expression)
    for e in expression:
        if e != ' ' and e != '.':
            exp, i = '', ''
            while e == '[' and i != ']':
                exp += i
                i = next(expression)
            j.append(exp)
N = int(input())
for i in range(N):
    n = [int(i) for i in input().split()]
    n_list.append(n)
for n in n_list:
    try:
        exp_out = hands[n[0]-1] + '(' + eyes[n[1]-1] + mouth[n[2]-1] + eyes[n[3]-1] + ')' + hands[n[4]-1]
    except IndexError:
        print('Are you kidding me? @\/@')
    else:
        print(exp_out)
