# !/usr/bin/env python

# _*_ coding: utf-8 _*_
"""
给定一个常数 K 以及一个单链表 L，请编写程序将 L 中每 K 个结点反转。例如：给定 L 为 1→2→3→4→5→6，K 为 3，则输出应该为 3→2→1→6→5→4；
如果 K 为 4，则输出应该为 4→3→2→1→5→6，即最后不到 K 个元素不反转。

输入格式：
每个输入包含 1 个测试用例。每个测试用例第 1 行给出第 1 个结点的地址、结点总个数正整数 N (≤10e5)、以及正整数 K (≤N)，
即要求反转的子链结点的个数。结点的地址是 5 位非负整数，NULL 地址用 −1 表示。

接下来有 N 行，每行格式为：

Address Data Next
其中 Address 是结点地址，Data 是该结点保存的整数数据，Next 是下一结点的地址。

输出格式：
对每个测试用例，顺序输出反转后的链表，其上每个结点占一行，格式与输入相同。

输入样例：
00100 6 4
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218

输出样例：
00000 4 33218
33218 3 12309
12309 2 00100
00100 1 99999
99999 5 68237
68237 6 -1
"""

original_list = []   # 输入链表
first_address, quantity, reverse_element = input().split()
for j in range(int(quantity)):
    son_chain = input().split()
    original_list.append(son_chain)


def creat_proper_list():   # 链表排序
    proper_list = []
    for i in range(int(quantity)):
        for son_cha in original_list:   # 寻找第一个节点
            if i == 0:
                if son_cha[0] == str(first_address):
                    proper_list.append(son_cha)
                    break
            else:
                if son_cha[0] == proper_list[i-1][2]:  # 添加后续节点
                    proper_list.append(son_cha)
                    break
    return proper_list


def creat_reverse_list():   # 反转顺序列表
    proper_list = creat_proper_list()
    proper_list_c = proper_list[::]

    for element in proper_list_c:
        if element[1] == reverse_element:
            element_index = proper_list.index(element)      # 寻找反转节点处的索引
            break
    for j in range(1, element_index + 1):  # 反转节点前的链表
        proper_list_c.insert(0, proper_list_c.pop(j))
        proper_list_c[0][2] = proper_list_c[1][0]
        proper_list_c[j][2] = proper_list_c[j+1][0]
    if element_index+1 <= (len(proper_list) - element_index - 1):
        for n in range(len(proper_list)-2, element_index, -1):   # 反转节点后的链表，从倒数第二位反向索引到反转节点位置
            proper_list_c.insert(len(proper_list_c), proper_list_c.pop(n))   # 并将每一个索引值添加到链表最后一位
            proper_list_c[n-1][2] = proper_list_c[n][0]
            proper_list_c[-2][2] = proper_list_c[-1][0]
            proper_list_c[-1][2] = '-1'
    return proper_list_c


for i in creat_reverse_list():
    print(' '.join(i))
exit(0)
