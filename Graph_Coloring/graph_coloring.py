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
# edges = [
#     (1, 1)
# ]
# edges = [
#     (1, 2),
#     (1, 3),
#     (2, 3)
# ]
# edges = [
# (1, 2),
# (1, 3),
# (1, 4),
# (2, 3),
# (2, 4),
# (3, 4)
# ]

neighbors = {}

#鄰居關係
for u, v in edges:
    if u == v:  #自己繞自己
        continue
    if u not in neighbors:
        neighbors[u] = []
    neighbors[u].append(v)

    if v not in neighbors:
        neighbors[v] = []
    neighbors[v].append(u)
# #如果被孤立
# all_nodes = set([u for u, v in edges] + [v for u, v in edges])
# for node in all_nodes:
#     if node not in neighbors:
#         neighbors[node] = []
# for test
#print("\nNeighbor relationships:")
#for node, neighbor_list in neighbors.items():
    #print(f"Node {node}: {neighbor_list}")
# 高到低排序
sorted_nodes = sorted(neighbors, key=lambda x: len(neighbors[x]), reverse=True)
# for test
#print("\nNeighbor relationships:")
#for node, neighbor_list in neighbors.items():
    #print(f"Node {node}: {neighbor_list}")
record = {}

for node in sorted_nodes: 
    colors = set () #set紀錄顏色且不會重複
    for neighbor in neighbors[node]:
        if neighbor in record:
            colors.add(record[neighbor]) #鄰居有幾個已經知道自己的顏色
    init = 0
    while init in colors:
        init = init+1

    record[node] = init

num_colors = len(set(record.values()))
print(num_colors)
