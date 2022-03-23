
# Imports
from random import randrange as rnd
import time

# Algorithims
def insertion_sort(test_array):
    for i in range(1, len(test_array)):
        key = test_array[i]
        j = i-1
        while j >= 0 and key < test_array[j]:
            test_array[j + 1] = test_array[j]
            j -= 1
            test_array[j + 1] = key


def merge(test_array,left,mid,right):
    s1 = mid-left+1
    s2 = right - mid
    L = [0] * (s1)
    R = [0] * (s2)

    for i in range(0, s1)
        L[i] = list[left+i]

    for j in range(0, s2)
        R[j] = list[mid + 1 + j]

    i = 0
    j = 0
    k = 1
    while i < s1 and j < s2:
        if L[i] <= R[j]:
            test_array[k] = L[i]
            i += 1
        else:
            test_array[k] = R[j]
            j += 1
        k += 1
    while i < s1:
        test_array[k] = L[i]
        i += 1
        k += 1
    while j < s2:
            test_array[k] = R[j]
            j += 1
            k += 1


def mergesort(test_array,left,right):
    if left < right:
       mid = left + (right - 1)//2
       mergesort(test_array, left, mid)
       mergesort(test_array, mid + 1, right)
       merge(test_array, left, mid, right)


def hybridsort(test_array):
    pass



def partition(list,left,right):
    pivot = list[right]
    i=left-1
    for j in range(left,right):
        if list[j] <= pivot:
            i=i+1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[right] = list[right], list[i+1]      
    return (i+1)      
    
    
def randomPartition(list,left,right):
       i=rnd(left,right) #generating random pivot index
       list[i], list[right] = list[right], list[i] #Swaping list[pivot] with list[last]
       return randomPartition(list,left,right)
       


def quicksort(list,left,right):
    if left < right:
        pivotIndex = partition(list,left,right)
        quicksort(list,left,pivotIndex-1)
        quicksort(list,pivotIndex+1,right)



def selectionsort(test_array):
    for i in range(len(test_array)):
        min_idx = i
        for j in range(i+1, len(test_array)):
            if test_array[min_idx] > test_array[j]:
                min_idx = j
        test_array[i], test_array[min_idx] = test_array[min_idx], test_array[i]


def hybridmergeandselectionsort(test_array):
    pass


# # NOTE:  Picking the Sizes of arrays and the how many arrays used at each size
# if __name__ == "__main__":
#     Samples = int(input("NO OF SAMPLES: "))
#     ValueOfSamples = []
#     for i in range(Samples):
#         ValueOfSamples.append(int(input(f"SIZE OF ARRAY {i+1} : ")))

#     # NOTE:  Picking Which ALgrothims to be used in sorting

#     print('''\n WHICH ALGROTHIMS DO YOU WANT TO BE COMPARED WITH EACH OTHER \n
#             1)QUICK SORT\n
#             2)MERGE SORT\n
#             3)SELECTION SORT\n
#             4)INSERTION SORT\n
#             5)HYBRID MERGE AND SELECTION SORT\n
#             ''')

#     Algos = int(input("NO OF ALGROTHIMS : "))
#     WhichAlgos = []
#     for i in range(Algos):
#         WhichAlgos.append(int(input(f"ALGROTHIM {i+1} (CHOOSE A NUMBER): ")))

#     # NOTE:Generation of random array at each size

#     TestArrays = []
#     for i in range(Samples):
#         ArrayToBeTested = []
#         for j in range(ValueOfSamples[i]):
#             Digit = random.randrange(0, ValueOfSamples[i])
#             # to make sure no repeated numbers
#             while ArrayToBeTested.count(Digit) == 0:
#                 ArrayToBeTested.append(Digit)
#         TestArrays.append(ArrayToBeTested)


# # testing
#     test_results = [[], [], [], [], []]
#     for i in range(Samples):
#         for j in range(len(WhichAlgos)):
#             if WhichAlgos[i] == 1:
#                 for k in range(len(TestArrays)):
#                     temp = TestArrays[i]
#                     begin = time.time()
#                     quicksort(temp,0,len(temp)-1)
#                     end = time.time()
#                     test_results[0].append(end-begin)
#             if WhichAlgos[i] == 2:
#                 for k in range(len(TestArrays)):
#                     temp = TestArrays[i]
#                     begin = time.time()
#                     mergesort(temp)
#                     end = time.time()
#                     test_results[1].append(end-begin)

#             if WhichAlgos[i] == 3:
#                 for k in range(len(TestArrays)):
#                     temp = TestArrays[i]
#                     begin = time.time()
#                     selectionsort(temp)
#                     end = time.time()
#                     test_results[2].append(end-begin)

#             if WhichAlgos[i] == 4:
#                 for k in range(len(TestArrays)):
#                     temp = TestArrays[i]
#                     begin = time.time()
#                     insertion_sort(temp)
#                     end = time.time()
#                     test_results[3].append(end-begin)

#             if WhichAlgos[i] == 5:
#                 for k in range(len(TestArrays)):
#                     temp = TestArrays[i]
#                     begin = time.time()
#                     hybridmergeandselectionsort(temp)
#                     end = time.time()
#                     test_results[4].append(end-begin)
# print(test_results)

testList = []
for j in range(10000):
    Digit = rnd(0,10000)
         # to make sure no repeated numbers
    while testList.count(Digit) == 0:
        testList.append(Digit)
                
# list=[8,1,6,4,2,3,9,5]
begin = time.time()
quicksort(testList,0,len(testList)-1)
end = time.time()
print('''Sorted list: {}\nExecution time = {}'''.format([0,1],end-begin))