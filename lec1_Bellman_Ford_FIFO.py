# coding:utf-8
# lec1 Bellman Ford Algorithm FIFO

import numpy as np
import matplotlib.pyplot as plt


def Bellman_Ford_FIFO(alllist_str, startNode, table):
    print('\n------------Bellman Ford Algorithm FIFO---------------')
    nodeNum = table.shape[0]  # 节点数量
    nodeList = list(alllist_str)  # ['a','b','c','d','e','f','g']  # 节点名称
    Q = []  # FIFO 先入先出队列
    Q.append(startNode)
    All = dict(zip(nodeList, [999] * nodeNum))  # 记录所有节点最短路径
    All[startNode] = 0
    Parent = dict(zip(nodeList, ['nil'] * nodeNum))  # 每个节点的父节点
    while Q:
        headQ = Q[0]  # 提取队列头
        del Q[0]  # 删除队列头
        headIndex = nodeList.index(headQ)
        # 松弛算法： relax
        for j in range(table.shape[1]):
            fromNode = headQ
            toNode = nodeList[j]
            relaxPath = All[fromNode] + table[headIndex, j]
            if relaxPath < All[toNode]:  # 如果松弛路径小于原有路径，则更新
                Parent[toNode] = fromNode  # 更新父节点
                All[toNode] = relaxPath
                if toNode not in Q:
                    Q.append(toNode)
        # print('NextQ= ', Q, 'Consider=', headQ, 'path=', All, 'parent=', Parent)
        print('NextQ= ', Q, 'Consider=', headQ, 'path=', [All[item] for item in All], 'parent=', [Parent[item] for item in Parent])

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
    print('------------Bellman Ford Algorithm FIFO Finished!---------\n')
    return All, Parent, state


if __name__ == '__main__':
    alllist_str = "sabcd"  # 节点名称 "1234567"
    startNode = 's'  # 起始节点
    table = [ [0,4,5,6,0], [0,0,2,0,0], [0,0,0,2,0], [0,-4,0,0,-3], [0,1,0,0,0] ]

    table = np.array(table)
    table[table == 0] = 999
    table[1,4] = 0  # 特殊路径，a->d = 0

    All, Parent, state = Bellman_Ford_FIFO(alllist_str, startNode, table)










