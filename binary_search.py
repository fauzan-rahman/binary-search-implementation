import time

def bruteforce_search(l, target):
    #example l = [1, 5, 7, 9]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, lower=None, higher=None):
    #example l = [1, 5, 7, 9]
    if lower is None:
        lower = 0
    if higher is None:
        higher = len(l)-1
    
    if higher<lower:
        return -1
    midpoint = (lower+higher) // 2
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, lower, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, higher)
    
if __name__ =='__main__':
    length = 10000
    l = []
    for i in range(length):
        l.append(i+1)
    target = int(input("Type a target number between 0-10,000. \n"))
    
    start = time.time()
    bruteforce_search(l, target)
    end = time.time()
    bruteforce_time = end-start
    print("Brute-Force Search time: ", bruteforce_time)
    
    start = time.time()
    binary_search(l, target)
    end = time.time()
    binary_time = end-start
    print("Binary Search time: ", binary_time)