def nim(n, a_moves, b_moves):
    def awin(i):
        for a_move in a_moves:
            if i>=a_move and not b_win[i-a_move]:
                a_win[i] = True 
                break
    def bwin(i):
        for b_move in b_moves:
            if i >= b_move and not a_win[i - b_move]:  
                b_win[i] = True
                break
    
    a_win = [False] * (n + 1)  
    b_win = [False] * (n + 1) 
         
    for i in range(1, n + 1): #i represents stone number
        #由小到大算每一步誰有決勝策略
        awin(i)
        bwin(i)
    
    if a_win[n]:
        print("A")
    else:
        print("B")

def process_input():
    x = int(input())
    cases = []
    for _ in range(x):
        n, m = map(int, input().split())
        a_moves = list(map(int, input().split()))
        b_moves = list(map(int, input().split()))
        cases.append((n, a_moves, b_moves))
    return cases

cases = process_input()
for n, a_moves, b_moves in cases:
    nim(n, a_moves, b_moves)
