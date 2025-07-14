from collections import deque,defaultdict
T = int(input())

for _ in range(T): #有幾筆測試資料
    n,m = map(int,input().split())
    w = list(map(int,input().split()))
    dependencies = defaultdict(list)
    in_degree = {i: 0 for i in range(n)}
    for _ in range(m):
        u,v = map(int, input().split())
        dependencies[u].append(v)
        in_degree[v] +=1
    
    queue = deque()
    earliest = {i:0 for i in range(n)} #find earilest to finish the task
    for i in range(n):
        if in_degree[i] ==0:
            queue.append(i)

    while queue:
        u = queue.popleft()
        for v in dependencies[u]:
            in_degree[v] -=1
            earliest [v] = max(earliest[v],earliest[u]+w[u])
            if in_degree[v] == 0:
                queue.append(v)

    weight = max(earliest[i] + w[i] for i in range(n))
    print (weight)
