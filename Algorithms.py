# This file includes 4 different ways to sort an array of data
# 1. QuickSort
# 2. MergeSort
# 3. SelectionSort
# 4. InsertionSort

# IDEA: why not add standard and our customized implementation and compare between them

class QuickSort:
    def quicksort(self, test_array):
        A = 3


class MergeSort:
    def mergesort(self, test_array):
        A = 3


class SelectionSort:
    def selectionsort(self, test_array):
        A = 3


class InsertionSort:
    def insertion_sort(self,test_array):
        for i in range(1, len(test_array)):
            key = test_array[i]
            j = i-1
            while j >= 0 and key < test_array[j]:
                test_array[j + 1] = test_array[j]
                j -= 1
            test_array[j + 1] = key



class HybridSort:
    def hybridsort(self, test_array):
        A = 3
