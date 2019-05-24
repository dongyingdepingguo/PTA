# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1044 火星数字 （20 分）
火星人是以 13 进制计数的：

地球人的 0 被火星人称为 tret。
地球人数字 1 到 12 的火星文分别为：jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec。
火星人将进位以后的 12 个高位数字分别称为：tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou。
例如地球人的数字 29 翻译成火星文就是 hel mar；而火星文 elo nov 对应地球数字 115。为了方便交流，请你编写程序实现地球和火星数字之间的互译。

输入格式：
输入第一行给出一个正整数 N（<100），随后 N 行，每行给出一个 [0, 169) 区间内的数字 —— 或者是地球文，或者是火星文。

输出格式：
对应输入的每一行，在一行中输出翻译后的另一种语言的数字。

输入样例：

4
29
5
elo nov
tam

输出样例：

hel mar
may
115
13
"""

n = int(input())
l = []
for i in range(n):
    l.append(input())
earth = [i for i in range(13)] + [13 * i for i in range(1, 13)]
mars = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov',
        'dec', 'tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
earth_mars = dict(zip(earth, mars))
mars_earth = dict(zip(mars, earth))
for i in l:

    try:
        word = int(i)
    except ValueError:
        mars_word = i
        if len(mars_word) > 4:
            mars_word = mars_word.split()
            trans_word = mars_earth[mars_word[0]] + mars_earth[mars_word[1]]
        else:
            trans_word = mars_earth[mars_word]
    else:
        earth_word = word
        h = int(earth_word / 13) * 13
        l = earth_word % 13
        if l != 0 and h != 0:
            trans_word = ' '.join([earth_mars[h], earth_mars[l]])
        elif l == 0 or h == 0:
            trans_word = earth_mars[h] if l == 0 else earth_mars[l]
        else:
            trans_word = earth_mars[h]
    finally:
        print(trans_word)
