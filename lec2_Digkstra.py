# coding:utf-8
# lec2 Digkstra's shortest-path algorithm

import numpy as np
import matplotlib.pyplot as plt


def Digkstra(alllist_str, startNode, table):
    print('\n------------Digkstra\'s shortest-path algorithm-----------')
    nodeNum = table.shape[0]  # 节点数量
    nodeList = list(alllist_str)  # ['a','b','c','d','e','f','g']  # 节点名称
    S = {}  # 闭列表，往里填东西
    Q = dict(zip(nodeList, [999]*nodeNum))  # 开列表，往外取东西
    Q[startNode] = 0
    All = Q.copy()  # 全部列表 = S + Q
    Parent = dict(zip(nodeList, ['nil'] * nodeNum))  # 每个节点的父节点
    while Q:
        # 找到目前Q中最小的节点
        minNode = min(Q, key=Q.get)  # 发现目前Q中最小节点
        minnodeIndex = nodeList.index(minNode)  # 最小节点索引
        S[minNode] = Q[minNode]  # 将该最小节点放入S中
        del Q[minNode]  # 删除Q中最小节点
        # qNode = list(Q.keys())
        # 松弛算法： relax
        for i in range(len(nodeList)):  # 对其余节点进行松弛操作
            toNode = nodeList[i]  # 其余每个节点的名称
            relaxPath = S[minNode] + table[minnodeIndex, i]  # from = minnode, to = i
            if relaxPath < All[toNode]:  # 如果松弛路径小于原有路径，则更新
                Parent[toNode] = minNode  # 更新父节点
                All[toNode] = relaxPath
                if toNode in Q.keys():
                    Q[toNode] = relaxPath  # 更新Q路径
                else:
                    S[toNode] = relaxPath  # 更新S路径(若有负路径)
        print('S=', S)
        print('Q=', Q)
        # print('Parent=', Parent)
        print('--------------------')
    print('Parent=', Parent)
    print('------------Digkstra\'s shortest-path algorithm Finished!-----------\n')
    return S, Q, Parent



if __name__ == '__main__':
    alllist_str = "suvxy"  # 节点名称 "1234567"
    startNode = 's'  # 起始节点
    table = [ [0,10,0,5,0], [0,0,1,2,0], [0,0,0,0,4], [0,3,9,0,2], [7,0,6,0,0] ]

    alllist_str = "sabcd"  # 节点名称 "1234567"
    startNode = 's'  # 起始节点
    table = [ [0,4,8,7,0], [0,0,0,0,8], [0,-6,0,4,6], [0,0,0,0,4], [0,0,0,0,0] ]

    table = np.array(table)
    table[table==0] = 999
    S, Q, Parent = Digkstra(alllist_str, startNode, table)










