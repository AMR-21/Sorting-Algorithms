
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


def merge(list, left, mid, right):
    nL = mid - left + 1
    nH = right - mid
    aL=[]
    aH=[]
    
    for i in range(left,mid+1):
        aL.append(list[i])
     
    for j in range(mid+1,right+1):
        aH.append(list[j])  
         
    i,j=0,0
    k=left
    while i<nL and j<nH:
        if aL[i] <= aH[j]:
            list[k]=aL[i]
            k+=1
            i+=1
        else:
            list[k]=aH[j]
            k+=1
            j+=1   
    while i<nL:
        list[k]=aL[i]
        k+=1
        i+=1
    while j<nH:
        list[k]=aH[j]
        k+=1
        j+=1


def mergeSort(test_array,left,right):
    if left < right:
       mid = (left+right)//2
       mergeSort(test_array, left, mid)
       mergeSort(test_array, mid + 1, right)
       merge(test_array, left, mid, right)



def hybridSort(list, left, right, limit):
    if len(list) == limit:
        selectionSort(list)
    else:
        if left < right:
            mid = (left+right)//2
            mergeSort(list, left, mid)
            mergeSort(list, mid + 1, right)
            merge(list, left, mid, right)

    



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
       


def quickSort(list,left,right):
    if left < right:
        pivotIndex = randomPivot(list,left,right)
        quickSort(list,left,pivotIndex-1)
        quickSort(list,pivotIndex+1,right)


def quickSelect(list,k,left,right):
    pivot=partition(list,left,right)
    if k==(pivot+1):
        return list[pivot]
    elif k < pivot:
        return quickSelect(list,k,left,pivot-1)
    else:
        return quickSelect(list,k,pivot+1,right)
     

'''Inesertion sort and selection sort'''

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i
        while j > 0 and key < list[j-1]:
            list[j] = list[j-1]
            j -= 1
        list[j] = key
            
            
def selectionSort(list):
    for i in range(len(list)-1):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        if i!=min_idx:
            list[min_idx] , list[i]= list[i] , list[min_idx]           
                

'''Test function'''
#def test(sizes):
 #   for size in sizes:
 #       print('Testing using sample of size =',size)
 #       rndList = rndUniqueList(size,0,200000)
 #       testList = deepcopy(rndList)
 #       begin = time()
  #      quickSort(testList,0,len(testList)-1)
 #       end = time()
 #       print('\nRunning time for Quick Sort is '+str((end-begin)*1000)+' ms')
 #       testList = deepcopy(rndList)
  #      begin = time()
 #       mergeSort(testList,0,len(testList)-1)  
 #      end = time()
 #       print('Running time for Merge Sort is '+str((end-begin)*1000)+' ms')
  #      testList = deepcopy(rndList)
  #      begin = time()
 #       selectionSort(testList)
 #       end = time()
 #       print('Running time for Selection Sort is '+str((end-begin)*1000)+' ms')
 #       testList = deepcopy(rndList)
 #       begin = time()
 #       insertionSort(testList)
 #       end = time()
  #      print('Running time for Insertion Sort is '+str((end-begin)*1000)+' ms\n\n')
 #       rndList.clear()

     
'''Test cases'''

# test([100,1000,5000,10000,25000,50000,100000])
# Randomly generated array with 50 unique items between 0 and 10000
arr = [7838, 5511, 7617, 2935, 4619, 5409, 8602, 1042, 5390, 45, 8110, 3545, 5761, 1666, 5165, 7909, 5178, 2881, 7013, 1104, 9763, 4813, 7043, 7048, 4996, 416, 7076, 5565, 4501, 4680, 5827, 
      644, 4566, 3433, 8059, 7132, 780, 7587, 9155, 302, 2742, 141, 7106, 2507, 367, 2384, 6272, 323, 148, 930]
#print(quickSelect(arr,8,0,len(arr)-1))
#arr = [5,8,25,16,13,124,1,88,75,44,64,32]
hybridSort(arr, 0, len(arr)-1,6)
print(arr)
# hybrid sort of the array 
# hybridSort(arr)
