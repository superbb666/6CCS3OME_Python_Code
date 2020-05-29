# coding:utf-8
# lec7 q2 branch and bound

import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt


def branch_and_bound(alllist_str, startNode, table):
    citylist = list(alllist_str)  # ['a','b','c','d','e','f','g']  # 城市名称
    city = table.shape[0]  # 城市数量
    index_start = citylist.index(startNode)
    boundingtree = {}  # 输出树

    for i in range(city):
        # 获取所有排列  [('a', 'b'), ('a', 'c'), ('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'b', 'e'), ...]
        combine = list(permutations(citylist, i+1))
        combine = [c for c in combine if c[0] == startNode]
        # print('com=', combine)
        for partial in combine:
            # 对路线表进行更新
            newtable = table.copy()
            for j in range(len(partial)-1):
                index1 = citylist.index(partial[j])
                index2 = citylist.index(partial[j+1])
                newtable[index1, :index2] = 999
                newtable[index1, index2+1:] = 999
                newtable[:index1, index2] = 999
                newtable[index1+1:, index2] = 999
                if not ( len(partial) == city and j == len(partial)-2 ):
                    newtable[index2, index_start] = 999

            # 计算bound结果
            leaving = newtable.min(axis=1)
            coming = newtable.min(axis=0)
            bounding = max([leaving.sum(), coming.sum()])
            boundingtree[partial] = bounding
            # 打印每次结果
            print('partial=', partial)
            # print(newtable)
            print('leaving=', leaving)
            print('coming', coming)
    # 输出全部结果
    print('boundingtree:\n', boundingtree)
    blist = list(boundingtree.items())
    for i in range(city):
        blayer = [layer for layer in blist if len(layer[0]) == i+1]
        for j in range(len(blayer)):
            text = str(blayer[j])
            print(text, end=" ")
        print('')
    final_layer = dict([layer for layer in blist if len(layer[0]) == city])
    print('final_layer', final_layer)
    minPath = min(final_layer, key=final_layer.get)
    print('The shortest path is:', minPath, boundingtree[minPath])
    return boundingtree



if __name__ == '__main__':
    alllist_str = "abcde"  # 城市名称 "1234567"
    startNode = 'a'  # TSP起始节点 (即终止节点)
    table = [[0,14,4,10,20], [14,0,7,8,7], [4,5,0,7,16], [11,7,9,0,2], [18,7,17,4,0]]

    table = np.array(table)
    table[table == 0] = 999

    boundingtree = branch_and_bound(alllist_str, startNode, table)





    '''
    # 画图
    print('boundingtree:\n', boundingtree)
    blist = list(boundingtree.items())
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, city*city)  # 设置x轴刻度的范围
    ax.set_ylim(-1*city, 1)  # 设置y轴刻度的范围

    for i in range(city):
        blayer = [layer for layer in blist if len(layer[0]) == i+1]
        for j in range(len(blayer)):
            text = str(blayer[j])
            print(text, end = " ")
            ax.annotate(text, xy=(5*j, -1*i), xytext=(5*j+0.01, -1*i+0.01), va='center', ha='center',
                        bbox= dict(boxstyle='round', fc='0.8') )
        print('')
    plt.show()
    '''




