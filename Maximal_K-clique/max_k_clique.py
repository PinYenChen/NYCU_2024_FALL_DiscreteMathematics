import itertools
import random
#邊的列表
edges = []

#讀取輸入直到 EOF
try:
    while True:
        #讀取一行輸入
        line = input().strip()
        #將輸入分割
        u, v = map(int, line.split())
        edges.append((u, v))
except EOFError:
    pass  #遇到EOF時結束輸入


#邊的列表
# edges = [
#     (0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (0, 8), (0, 13), (1, 3), (1, 4), 
#     (1, 5), (1, 7), (1, 8), (1, 10), (1, 11), (1, 13), (2, 3), (2, 5), (2, 6), 
#     (2, 11), (2, 12), (3, 6), (3, 7), (3, 12), (3, 14), (4, 5), (4, 6), (4, 7), 
#     (4, 8), (4, 9), (4, 10), (4, 12), (4, 13), (5, 7), (5, 9), (5, 10), (6, 7), 
#     (6, 14), (7, 8), (7, 9), (7, 11), (7, 14), (8, 9), (8, 13), (8, 14), (9, 10), 
#     (9, 11), (9, 13), (10, 11), (10, 12), (10, 13), (10, 14), (11, 12), (11, 14), 
#     (12, 13), (13, 14)
# ]

############################################# method 1 tle
# 鄰居關係
# for u, v in edges:
#     if u == v:  # 自己繞自己
#         continue
#     if u not in neighbors:
#         neighbors[u] = []
#     neighbors[u].append(v)

#     if v not in neighbors:
#         neighbors[v] = []
#     neighbors[v].append(u)

# def is_clique(subneighbor, neighbors):
#     for u in subneighbor:
#         for v in subneighbor:
#             if u != v and (v not in neighbors[u] or u not in neighbors[v]):
#                 return False
#     return True

# def find_cliques(neighbors):
#     max_cliques = set()  # 使用集合避免重複的子圖
#     k = 3

#     while True:
#         cur_cliques = []
#         nodes = list(neighbors.keys())
#         for node in nodes:
#             possible_nodes = [node] + neighbors[node]
#             for sub in itertools.combinations(possible_nodes, k):  # 找出大小為 k 的子圖
#                 if is_clique(sub, neighbors):
#                     cur_cliques.append(set(sub))

#         # 過濾掉可以擴展的 clique
#         filtered_cliques = []
#         for cli in cur_cliques:
#             can_expand = False
#             for neighbor in neighbors.keys():
#                 if neighbor not in cli and cli.issubset(set(neighbors[neighbor]) | {neighbor}):
#                     can_expand = True
#                     break
#             if not can_expand:  # 如果不能擴展為更大的 clique 才加進去filter內
#                 filtered_cliques.append(set(cli))

#         # 如果找到新的極大 clique，輸出並記錄
#         if filtered_cliques:
#             print(k)
#             for fil in sorted(filtered_cliques, key=lambda x: sorted(x)):
#                 sorted_clique = sorted(fil)  # 確保升序
#                 clique_str = "{" + ", ".join(map(str, sorted_clique)) + "}"  # 格式化為大括號
#                 if frozenset(sorted_clique) not in max_cliques:
#                     print(clique_str)
#                     max_cliques.add(frozenset(sorted_clique))
#         if not filtered_cliques:
#             break
#         k += 1
######################################## method2 tle
# def built_neighbor(edges, n):
#     adjacent = [[0]*n for i in range(n)]
#     for u,v in edges:
#         adjacent[u][v] =1
#         adjacent[v][u] =1
#     return adjacent

# def is_clique(adjacent, nodes):
#     for i in nodes:
#         for j in nodes:
#             if i!=j and (adjacent[i][j] == 0 or adjacent[j][i] == 0) :
#                 return False
#     return True
            
# def find_cliques(edges, n):
#     adjacent = built_neighbor(edges, n)
#     max_cliques = set()
#     k =3

#     found = True
#     while found: 
#         cur_cliques = []
#         for possible in itertools.combinations(range(n),k): #n取k
#             if is_clique(adjacent, possible):
#                 #print("here")
#                 cur_cliques.append(set(possible)) #用set裝進去
#         filtered_cliques = [] #用來過濾可能可以擴展更大的
        
#         for cli in cur_cliques:
            
#             can_expand = False
#             for i in range(n):
#                 if i not in cli and cli.issubset(set(j for j, connected in enumerate(adjacent[i]) if connected)):
#                     can_expand = True
#                     break
#             if not can_expand:
#                 filtered_cliques.append(cli)

#         # 輸出極大 clique
#         if filtered_cliques:
#             print(k)
#             for fil in filtered_cliques:
#                 clique_str = "{" + ", ".join(map(str, sorted(fil))) + "}"
#                 if frozenset(fil) not in max_cliques:
#                     print(clique_str)
#                     max_cliques.add(frozenset(fil))
#         if not filtered_cliques:
#             found = False
#         k += 1            


# n = max(max(u, v) for u, v in edges)+1
# #print (n)
# # 呼叫函數
# find_cliques(edges , n)

#bron
def build_neighbors(edges):
    neighbors = {}
    for u, v in edges:
        if u not in neighbors:
            neighbors[u] = set()
        if v not in neighbors:
            neighbors[v] = set()
        neighbors[u].add(v)
        neighbors[v].add(u)
    return neighbors
def choose_pivot(p,x):
    intersection = p.intersection(x)
    if intersection:
        u = random.choice(list(intersection))
        return u
    else:
        return None

def bron_kerbosch(r, p, x, neighbors, cliques):
    if not p and not x:  # 當P和X都是空集合時，R是一個極大團
        cliques.append(r)
        return

    pivot = choose_pivot(p, x)
    if pivot is not None:
        # 使用pivot進行節點選擇
        p_without_pivot = p - neighbors[pivot]
    else:
        p_without_pivot = p

    for v in list(p_without_pivot):
        bron_kerbosch(
            r.union({v}),  
            p.intersection(neighbors[v]),#更新P為v的鄰居
            x.intersection(neighbors[v]),#更新X為v的鄰居
            neighbors,
            cliques
        )
        p.remove(v)#從P中移除已處理的節點
        x.add(v)   #表示已被考慮過

def find_maximal_cliques(edges):
    neighbors = build_neighbors(edges)

    # 初始化 P, R 和 X
    p = set(neighbors.keys())#候選節點集合
    r = set()                #當前團
    x = set()                #已處理過的節點
    cliques = []             #儲存所有極大團

    bron_kerbosch(r, p, x, neighbors, cliques)
    cliques_sorted = sorted(cliques, key=lambda clique: tuple(sorted(clique)))

    max_len_in_clique = max(len(clique) for clique in cliques)
    set_max = set()
    for clique in cliques:
        set_max.add(len(clique))
    #print(max_len_in_clique)
    # 輸出極大團
    k = 3
    while k <= max_len_in_clique:
        if k in set_max:
            print (k) #maybe 會有6但沒有５的狀況發生
        
        for clique in cliques_sorted:
            if len(clique) == k:                
                clique_str = "{" + ",".join(map(str, sorted(clique))) + "}"
                print(clique_str)
        k+=1

find_maximal_cliques(edges)
