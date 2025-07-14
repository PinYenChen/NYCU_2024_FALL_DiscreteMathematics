import random
import sys
import heapq
t = int(input())
def build_matrix(n,m):
    
    # adjacent = [[0]*n for i in range(n)]
    # for j in range(m):
    #     line = input().strip()
    #     u,v,w = map(int, line.split())
    #     adjacent[u][v] = w
    #     adjacent[v][u] = w
    #too slow 用list
    adjacent = [[] for i in range(n)]
    edges = []
    for _ in range(m):
        line = input().strip()
        u,v,w = map(int,line.split())
        adjacent[u].append((w,v))
        adjacent [v].append((w,u))

    return adjacent

def find_mst(key, visited,adjacent,n):
    weight = 0
    key[0] = 0 #from 0 start

    # for i in range(n): #need n time to find the path
    #     u = -1
    #     for i in range(n):#找到key中最小的點
    #         if not visited[i] and (u==-1 or key[i]<key[u]): #key[-1]會抓倒數第一個
    #             u = i
        
    #     if key[u] == float('inf'): #表示沒有路可以走
    #         return -1
    #     else:
    #         visited[u]= True
    #         weight = weight +key[u]
    #         for v in range(n): #update the graph
    #             if adjacent[u][v] != 0 and not visited [v] and adjacent [u][v] <key[v]:
    #                 key[v] = adjacent [u][v]

    #heapsort
    min_heap = [(0,0)] #from 0 start
    while min_heap: #min_heap不是空的話就繼續
        current, u = heapq.heappop(min_heap) #從min_heap拿出最小的weight跟其編號 for speedup
        if visited[u]:
            continue #to skip the point since it has been processed
        else:
            visited[u] = True
            weight = weight + current
            for w,v in adjacent[u]:
                if not visited[v] and w<key[v]:
                    key[v] = w
                    heapq.heappush(min_heap,(w,v))
    # path = 0
    # for x in range(n): #check whether all points are processed
    #     if visited[x] == True:
    #         path +=1
    # if (path ==n):
    #     return weight
    # else: return -1
    if all(visited):
        return weight
    else:
        return -1


for i in range(t):
    line = input().strip()
    n,m =  map(int, line.split())
    adjacent = build_matrix(n,m)
    #pre = [-1]*n
    key = [float('inf')] * n
    visited = [False]*n

    print (find_mst(key, visited,adjacent,n))
