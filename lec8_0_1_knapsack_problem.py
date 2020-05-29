# coding:utf-8
# lec8 additional 0-1 Knapsack Problem

import numpy as np
import matplotlib.pyplot as plt


def Knapsack(W, table):
    # 对table进行处理
    if len(table[0]) == 2:  # 未计算v/w
        for i in range(len(table)):
            table[i].append( table[i][0] / table[i][1] )
    table = sorted(table, key=lambda item:item[2], reverse=True)  # 按照v/w降序排序
    print('table=', table)
    items = len(table)
    table.append([0,10000,0])   # 添加一个极重的物体作为循环终止
    [Prom, UnProm, UnConsid] = [0, 1, 2]  # 节点状态
    init = [layer, index, lastlayer, bagvalue, bagweight, best, bestindex, k, bound, state] = \
            [0,     0,     (0,0),     0,        0,        0,    (0,0),     0, 100000, UnProm]
    # 层，每层索引，上层编号，包内价值，包内重量，最优重量，bound_k，边界，节点状态
    print('[layer, index, lastlayer, bagvalue, bagweight, best, bestindex,  k,    bound,  state]')
    tree = []
    tree.append(init)
    tree.append([1,2] + init[2:-1] + [UnConsid])
    tree.append([1,1] + init[2:-1] + [UnConsid])
    consider = 1  # 有需要考虑的节点
    while consider:
        consider = 0
        for i in range(len(tree)-1, -1, -1):
            if tree[i][-1] == UnConsid:
                consider = i
                break
        if consider == 0:
            break
        [layer, index, lastlayer, bagvalue, bagweight] = tree[consider][:5]  # 待处理节点的信息
        # [layer, index, lastlayer, bagvalue, bagweight, best, bestindex, k, bound, state] = tree[consider]
        #  0,     1,     2,         3,        4,         5,    6,         7, 8,     9
        # 往背包里加东西
        if index % 2 == 1:
            bagvalue = bagvalue + table[layer-1][0]
            bagweight = bagweight + table[layer-1][1]
        # 计算best solution
        allbest = max([node[3] for node in tree if node[4] <= W])  # 全局最优bestvalue
        if bagweight <= W and bagvalue > allbest:
            best = bagvalue
            bestindex = (layer, index)
        # 计算k
        kweight = bagweight  # 循环放item，直到溢出W
        for knum in range(layer, items):
            kweight = kweight + table[knum][1]
            if kweight > W:
                k=knum + 1
                break
        if kweight <= W:
            k = items + 1
        # 计算bound
        kvalue = 0
        kweight = bagweight
        for j in range(layer, k-1):
            kvalue = kvalue + table[j][0]
            kweight = kweight + table[j][1]
        bound = (bagvalue + kvalue) + (W - kweight) * table[k-1][2]
        # 计算状态
        if bound <= best or bagweight > W:
            state = UnProm
        else:
            state = Prom
        # 更新该节点全部信息
        tree[consider] = [layer, index, lastlayer, bagvalue, bagweight, best, bestindex, k, bound, state]
        # 打印节点
        formatting = "{0[0]:<5}{0[1]:<5}{1:<11}{0[3]:<10}{0[4]:<10}{0[5]:<7}{2:<11}{0[7]:<5}{0[8]:<10.2f}{0[9]:<5} "
        formatting = "layer={0[0]:<5}, index={0[1]:<5}, lastlayer={1:<11}, bagvalue={0[3]:<5}, bagweight={0[4]:<5}, best={0[5]:<5}, bestindex={2:<11}, k={0[7]:<5}, bound={0[8]:<10.2f}, state={0[9]:<5} "
        print('tree=', formatting.format(tree[consider], str(tree[consider][2]), str(tree[consider][6])))
        # print('tree=', tree[consider])
        # 添加子节点
        if state == Prom and layer <= items-1:
            newlayer = layer + 1
            newindex = [node[1] for node in tree if node[0] == newlayer]  # 获取该层索引号排到哪儿了
            if newindex:  # 如果索引号不为空
                newindex = max(newindex)
            else:
                newindex = 0
            noderight = [newlayer, newindex + 2, (layer, index)] + tree[consider][3:-1] + [UnConsid]
            nodeleft = [newlayer, newindex + 1, (layer, index)] + tree[consider][3:-1] + [UnConsid]
            tree.append(noderight)
            tree.append(nodeleft)
    return


if __name__ == '__main__':
    """主函数"""
    W = 16  # 背包限重
    table = [[40,2,20], [30,5,6], [50,10,5], [10,5,2]]  # 待放货物, v, w, v/w

    Knapsack(W, table)





