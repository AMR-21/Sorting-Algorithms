
# Imports
from random import randrange as rnd
from time import time
from copy import deepcopy

def rndUniqueList(size,min,max):
    list = []
    i=1
    while i<=size:
        digit = rnd(min,max+1)
        # to make sure no repeated numbers
        if list.count(digit) == 0:
            list.append(digit)
        else:
            i-=1
        i+=1       
    return list        


'''Algorithms'''
'''Merge sort and hybrid merge sort'''

def merge(list,left,mid,right):
    s1 = mid-left+1
    s2 = right - mid
    L = [0] * (s1)
    R = [0] * (s2)

    for i in range(0, s1):
        L[i] = list[left+i]

    for j in range(0, s2):
        R[j] = list[mid + 1 + j]

    i = 0
    j = 0
    k = 0
    while i < s1 and j < s2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while i < s1:
        list[k] = L[i]
        i += 1
        k += 1
    while j < s2:
        list[k] = R[j]
        j += 1
        k += 1


def mergesort(list,left,right):
    if left < right:
       mid = (left + (right - 1))//2
       mergesort(list, left, mid)
       mergesort(list, mid + 1, right)
       merge(list, left, mid, right)


def hybridsort(list):
    pass



'''Quick sort and Quick select'''

def partition(list,left,right):
    pivot = list[right]
    i=left-1
    for j in range(left,right):
        if list[j] <= pivot:
            i=i+1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[right] = list[right], list[i+1]      
    return (i+1)      
    
    
def randomPivot(list,left,right):
       i=rnd(left,right) #generating random pivot index
       list[i], list[right] = list[right], list[i] #Swaping pivot with last item
       return partition(list,left,right)
       


def quicksort(list,left,right):
    if left < right:
        pivotIndex = randomPivot(list,left,right)
        quicksort(list,left,pivotIndex-1)
        quicksort(list,pivotIndex+1,right)


def findK(list,k):
    pivot=list[partition(list,0,len(list)-1)]
    aL = []
    aR = []
    for i in range(len(list)):
        if list[i] < pivot:
            aL.append(list[i])
        elif  list[i] > pivot:
            aR.append(list[i])  
    if k <=  len(aL):
        return findK(aL,k)
    elif k > len(list) - len(aR):
        return findK(aR,k - (len(list) - len(aR)))
  
    return pivot 


'''Inesertion sort and selection sort'''

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
            list[j + 1] = key
            
            
def selectionSort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j

'''Test function'''
def test(sizes):
    for size in sizes:
        print('Testing using sample of size =',size)
        rndList = rndUniqueList(size,0,20000)
        testList = deepcopy(rndList)
        begin = time()
        quicksort(testList,0,len(testList)-1)
        end = time()
        print('\nRunning time for Quick Sort is '+str((end-begin)*1000)+' ms')
        # testList = deepcopy(rndList)
        # begin = time()
        # mergesort()
        # end = time()
        # print('Running time for Merge Sort is '+str((end-begin)*1000)+' ms')
        testList = deepcopy(rndList)
        begin = time()
        selectionSort(testList)
        end = time()
        print('Running time for Selection Sort is '+str((end-begin)*1000)+' ms')
        testList = deepcopy(rndList)
        begin = time()
        insertionSort(testList)
        end = time()
        print('Running time for Insertion Sort is '+str((end-begin)*1000)+' ms\n\n')
     
'''Test cases'''
# test([1000,10000,25000,50000,100000])
testList=[8,7,6,5,4,3,2,1]
mergesort(testList,0,len(testList)-1)
print(testList)
