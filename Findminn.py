__author__ = "Claytonbat"
from random import randrange
import time
def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist :
            if i > j:
                issmallest = False
        if  issmallest:
                overallmin = i
    return overallmin

def findMin1(alist):
    temp_min = alist[0]
    for i in alist:
        if temp_min > i:
            temp_min = i
    return temp_min

#print(findMin([5,4,3,2,1,0]))
for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print (findMin(alist))
    end = time.time()
    start1 = time.time()
    print (findMin1(alist))
    end1 = time.time()
    print ("Size: %d time O(n): %f,  time O(n2): %f" %(listSize, (end1 - start1), (end - start)))
