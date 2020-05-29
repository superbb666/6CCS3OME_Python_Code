# coding:utf-8
# lec1 Bellman Ford Algorithm

import numpy as np
import matplotlib.pyplot as plt
from lec1_Bellman_Ford import Bellman_Ford
from lec1_Bellman_Ford_FIFO import Bellman_Ford_FIFO
from lec2_Digkstra import Digkstra
from lec3_Johnson import Johnson
from lec7_branch_and_bound import branch_and_bound
from lec8_0_1_knapsack_problem import Knapsack


if __name__ == '__main__':

    alllist_str = "suvxy"  # 节点名称 "1234567"
    startNode = 's'  # 起始节点
    table = [ [0,10,0,5,0], [0,0,1,2,0], [0,0,0,0,4], [0,3,9,0,2], [7,0,6,0,0] ]  # Bellman_Ford
    # table = [[0,14,4,10,20], [14,0,7,8,7], [4,5,0,7,16], [11,7,9,0,2], [18,7,17,4,0]]  # branch_and_bound

    #table = [[0, 3, -2, 0, -4], [0, 0, 0, 1, 7], [0, 4, 0, 0, 0], [2, 0, -5, 0, 0], [0, 0, 0, 6, 0]]  # Johnson
    addNode = 'A'  # 新增起始节点
    addPath = [0, 0, 0, 0, 0]



    alllist_str = "sabck"  # 节点名称 "1234567"
    startNode = 's'  # 起始节点
    table = [ [0,10,0,5,0], [0,0,1,3,5], [0,0,0,0,2], [0,2,4,0,0], [0,0,4,6,0] ]




    table = np.array(table)
    table[table == 0] = 999
    # table[1, 4] = 0  # 特殊路径，a->d = 0

    # All, Parent, state = Bellman_Ford(alllist_str, startNode, table)
    # All, Parent, state = Bellman_Ford_FIFO(alllist_str, startNode, table)
    # S, Q, Parent = Digkstra(alllist_str, startNode, table)
    # newtable = Johnson(alllist_str, table, addNode, addPath)
    # boundingtree = branch_and_bound(alllist_str, startNode, table)

    W = 22  # 背包限重
    # table = [[40,2,20], [30,5,6], [50,10,5], [10,5,2]]  # 待放货物, v, w, v/w  # 0_1_knapsack_problem
    table = [[70,14], [60,15], [40,10], [15,5], [10,5]]  # 待放货物, v, w, v/w  # 0_1_knapsack_problem

    Knapsack(W, table)






