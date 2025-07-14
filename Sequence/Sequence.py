#homework1-2
"""
def possibilities (total, start, count): #cur,all
    # terminal conditions
    if (total == 0):
        #all_seq.append(list(current_seq))
        count[0] +=1
        return 
    else:
        for i in range (start, total+1):
            #current_seq.append(i)
            possibilities(total-i, i+1,  count) # i+1 到total-i有多拗可能性  #current_seq, all_seq,
            #current_seq.pop() #把當期的pop掉，才可以去試其他可能

def answer(l):
    #cur_seq = []
    #seq = []
    count = [0]
    possibilities(l, 1,  count ) #cur_seq, seq,
    #for i in (seq): for printing the answer
        #print (i) 
    return count[0]  #"the total number of the increasing sequences is


x = int(input()) #x is number of test
for j in range(1,x+1):
    l = int(input())
    print(answer(l))
"""
#initialization
def initial():
    table = [[0]*301 for i in range(301)]
    for i in range(301):
        table[0][i] =1 #total 0 最大選擇k的方法只有一種
    
    for i in range(301):  #使用的最大數字
        for j in range(1,301):#total
            table[j][i] += table[j][i-1] #不使用i
            #使用i的情況
            if (j>=i): #當total>=要選擇的數，該項才有職
                table[j][i]+= table[j-i][i-1]
    
    return table

table = initial()

x = int(input()) #x is number of test
for j in range(1,x+1):
    l = int(input())
    print(table[l][l])
