# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。现在给出应该输入的一段文字、以及实际被输入的文字，
请你列出肯定坏掉的那些键。

输入格式：
输入在 2 行中分别给出应该输入的文字、以及实际被输入的文字。每段文字是不超过 80 个字符的串，由字母 A-Z（包括大、小写）、
数字 0-9、以及下划线 _（代表空格）组成。题目保证 2 个字符串均非空。

输出格式：
按照发现顺序，在一行中输出坏掉的键。其中英文字母只输出大写，每个坏键只输出一次。题目保证至少有 1 个坏键。

输入样例：
7_This_is_a_test
_hs_s_a_es

输出样例：
7TI
"""

original_char = input()
error_char = input()

n = 0
bad_key = []
for i, j in enumerate(original_char):

    try:
        r = error_char[i - n]
    except IndexError as e:
        r = error_char[i - n - 1]
    finally:
        if j != r:
            n += 1
            j = j.upper()
            if j not in bad_key:
                bad_key.append(j)
print(''.join(bad_key))