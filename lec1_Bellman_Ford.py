# coding:utf-8
# lec1 Bellman Ford Algorithm

import numpy as np
import matplotlib.pyplot as plt


def Bellman_Ford(alllist_str, startNode, table):
    print('\n------------Bellman Ford Algorithm---------------')
    nodeNum = table.shape[0]  # 节点数量
    nodeList = list(alllist_str)  # ['a','b','c','d','e','f','g']  # 节点名称
    All = dict(zip(nodeList, [999] * nodeNum))  # 记录所有节点最短路径
    All[startNode] = 0
    Parent = dict(zip(nodeList, ['nil'] * nodeNum))  # 每个节点的父节点
    for node in range(nodeNum):
        # 松弛算法： relax
        for i in range(table.shape[0]):
            for j in range(table.shape[1]):
                fromNode = nodeList[i]
                toNode = nodeList[j]
                relaxPath = All[fromNode] + table[i, j]
                if relaxPath < All[toNode]:  # 如果松弛路径小于原有路径，则更新
                    Parent[toNode] = fromNode  # 更新父节点
                    All[toNode] = relaxPath
        print('------loop ', node, ': ', nodeList[node], '----------')
        print('All=', All)
        print('Parent=', Parent)
    print('Final Parent=', Parent)

    # 检测负向环
    state = True
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            fromNode = nodeList[i]
            toNode = nodeList[j]
            if All[toNode] > All[fromNode] + table[i, j]:
                state = False
                break
    print('No negative cycles? ', state)
    print('------------Bellman Ford Algorithm  Finished!---------\n')
    return All, Parent, state


if __name__ == '__main__':
    alllist_str = "suvxy"  # 节点名称 "1234567"
    startNode = 's'  # 起始节点
    table = [ [0,10,0,5,0], [0,0,1,2,0], [0,0,0,0,4], [0,3,9,0,2], [7,0,6,0,0] ]

    table = np.array(table)
    table[table == 0] = 999

    All, Parent, state = Bellman_Ford(alllist_str, startNode, table)










