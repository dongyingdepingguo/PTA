# !/usr/bin/env python

# _*_ coding: utf-8 _*_

"""
1003 我要通过！ （20 分）
“答案正确”是自动判题系统给出的最令人欢喜的回复。本题属于 PAT 的“答案正确”大派送 —— 只要读入的字符串满足下列条件，系统就输出“答案正确”，
否则输出“答案错误”。

得到“答案正确”的条件是：

字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。

输入格式：
每个测试输入包含 1 个测试用例。第 1 行给出一个正整数 n (<10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。

输出格式：
每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。

输入样例：

8
PAT
PAAT
AAPATAA
AAPAATAAAA
xPATx
PT
Whatever
APAAATAA

输出样例：

YES
YES
YES
YES
NO
NO
NO
NO
"""

N = int(input())
test_list = []
for i in range(N):
    test_list.append(input())
for test_char in test_list:
    if test_char in ['PAT', 'PAAT']:
        print('YES')
    else:
        char_split = test_char.split('P')
        if len(char_split) != 2:
            print('NO')
        else:
            A1, TA1 = char_split
            char_split2 = TA1.split('T')
            if len(char_split2) != 2:
                print('NO')
            else:
                A2, A3 = char_split2
                if (len(A1)*'A' != A1) or (len(A2)*'A' != A2) or (len(A3)*'A' != A3) or len(A2) == 0:
                    print('NO')
                else:
                    if len(A1) == 0 and len(A3) == 0:
                        print('YES')
                    else:
                        if len(A3)/ len(A1) == len(A2):
                            print('YES')
                        else:
                            print('NO')
