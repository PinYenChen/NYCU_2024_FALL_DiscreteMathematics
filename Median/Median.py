import heapq
n = int(input())
#sample = []
max_heap = []
min_heap = []

for _ in range(n):
    behavior, num = input().split()
    num = int(num)

    # if behavior == 'a':
    #     sample.append(num)
    # elif behavior == 'd' and num in sample:
    #     sample.remove(num)

    # sample.sort()
    # length = len(sample)
    # if length%2 ==0:
    #     print((sample[length // 2 - 1] + sample[length // 2]) / 2)
    # else:
    #     print(sample[length // 2])
    if behavior == 'a':

        #heap 最左邊是最小值，所以進max_heap數要加付好since we want max_heap[0]is the max
        #[5,6,7,8] ==> [-5, -6, -7,-8] ==> [-8,-7,-6,-5] ==> -(-)8 is the max

        if len(max_heap) ==0 or num<= -max_heap[0]: #initial or <=min_heap裡的最小值
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

    elif behavior == 'd':
        if num <= -max_heap[0]:
            max_heap.remove(-num)
            heapq.heapify(max_heap)     
        else:
            min_heap.remove(num)
            heapq.heapify(min_heap)

    #check the length of two heaps
    if len(max_heap) > (len(min_heap) +1):
        max_element = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, max_element)
    elif len(min_heap) > (len(max_heap)):
        min_element = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_element)

    #find median
    if len(max_heap) > len(min_heap):
        result = -max_heap[0]
    #elif len(min_heap) >len(max_heap):
        #result = min_heap[0]
    elif(len(max_heap) == len(min_heap)):
        result = (-max_heap[0] + min_heap[0])//2
    # for heap in max_heap:
    #     print(-heap)
    # print("this is min_heap")
    # for heap in min_heap:
    #     print (heap)
    print (result)
