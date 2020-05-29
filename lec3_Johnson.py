# coding:utf-8
# lec3 Johnson's Algorithm

import numpy as np
import matplotlib.pyplot as plt
from lec1_Bellman_Ford import Bellman_Ford

def Johnson(alllist_str, table, addNode, addPath):
    print('\n------------Johnson\'s Algorithm---------------')
    startNode = addNode  # 将新增节点作为起始节点
    nodeList = list(alllist_str)  # ['a','b','c','d','e','f','g']  # 节点名称
    # 将新增节点加入表格中
    addtable = np.row_stack((addPath, table))  # s到其他点的距离为0
    addtable = np.column_stack(([999]*(len(addPath)+1), addtable))  # 其他点到不了s
    new_alllist_str = startNode + alllist_str
    print('addtable=\n', addtable)
    # 计算各个节点最优解
    All, Parent, state = Bellman_Ford(new_alllist_str, startNode, addtable)
    # 重新计算权重
    if not any(addPath):  # 如果路径全为0
        newtable = np.zeros(table.shape)
        for i in range(table.shape[0]):
            for j in range(table.shape[1]):
                fromNode = nodeList[i]
                toNode = nodeList[j]
                newtable[i,j] = table[i,j] + All[fromNode] - All[toNode]   # w=w+u-v
    else:
        newtable = np.zeros(table.shape)
        for i in range(table.shape[0]):
            for j in range(table.shape[1]):
                fromPath = addPath[i]
                toPath = addPath[j]
                newtable[i,j] = table[i,j] - toPath + fromPath  # w=w-u+v
    newtable[newtable>900] = -999

    print('newtable=\n', newtable)
    return newtable


if __name__ == '__main__':
    alllist_str = "12345"  # 节点名称 "1234567"
    table = [ [0,3,-2,0,-4], [0,0,0,1,7], [0,4,0,0,0], [2,0,-5,0,0], [0,0,0,6,0] ]
    addNode = 's'  # 起始节点
    addPath = [0,0,0,0,0]

    table = np.array(table)
    table[table==0] = 999

    newtable = Johnson(alllist_str, table, addNode, addPath)











