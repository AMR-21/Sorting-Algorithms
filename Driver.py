
# Imports
import random
import matplotlib.pyplot as plt
import numpy as np
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


def mergesort(test_array):
    pass


def hybridsort(test_array):
    pass


def quicksort(test_array):
    pass


def selectionsort(test_array):
    for i in range(len(test_array)):
        min_idx = i
        for j in range(i+1, len(test_array)):
            if test_array[min_idx] > test_array[j]:
                min_idx = j
        test_array[i], test_array[min_idx] = test_array[min_idx], test_array[i]


def hybridmergeandselectionsort(test_array):
    pass


# NOTE:  Picking the Sizes of arrays and the how many arrays used at each size
if __name__ == "__main__":
    Samples = int(input("NO OF SAMPLES: "))
    ValueOfSamples = []
    for i in range(Samples):
        ValueOfSamples.append(int(input(f"SIZE OF ARRAY {i+1} : ")))

    # NOTE:  Picking Which ALgrothims to be used in sorting

    print('''\n WHICH ALGROTHIMS DO YOU WANT TO BE COMPARED WITH EACH OTHER \n
            1)QUICK SORT\n
            2)MERGE SORT\n
            3)SELECTION SORT\n
            4)INSERTION SORT\n
            5)HYBRID MERGE AND SELECTION SORT\n
            ''')

    Algos = int(input("NO OF ALGROTHIMS : "))
    WhichAlgos = []
    for i in range(Algos):
        WhichAlgos.append(int(input(f"ALGROTHIM {i+1} (CHOOSE A NUMBER): ")))

    # NOTE:Generation of random array at each size

    TestArrays = []
    for i in range(Samples):
        ArrayToBeTested = []
        for j in range(ValueOfSamples[i]):
            Digit = random.randrange(0, ValueOfSamples[i])
            # to make sure no repeated numbers
            while ArrayToBeTested.count(Digit) == 0:
                ArrayToBeTested.append(Digit)
        TestArrays.append(ArrayToBeTested)


# testing
    test_results = [[], [], [], [], []]
    for i in range(len(Samples)):
        for j in range(len(WhichAlgos)):
            if WhichAlgos[i] == 1:
                for k in range(len(TestArrays)):
                    begin = time.time()
                    quicksort(TestArrays[i])
                    end = time.time()
                    test_results[i].append(end-begin)
            if WhichAlgos[i] == 2:
                for k in range(len(TestArrays)):
                    begin = time.time()
                    mergesort(TestArrays[i])
                    end = time.time()
                    test_results[i].append(end-begin)

            if WhichAlgos[i] == 3:
                for k in range(len(TestArrays)):
                    begin = time.time()
                    selectionsort(TestArrays[i])
                    end = time.time()
                    test_results[i].append(end-begin)

            if WhichAlgos[i] == 4:
                for k in range(len(TestArrays)):
                    begin = time.time()
                    insertion_sort(TestArrays[i])
                    end = time.time()
                    test_results[i].append(end-begin)

            if WhichAlgos[i] == 5:
                for k in range(len(TestArrays)):
                    begin = time.time()
                    hybridmergeandselectionsort(TestArrays[i])
                    end = time.time()
                    test_results[i].append(end-begin)
    # visualization
    plt.title("Running Times")
    x = ValueOfSamples
    plt.xlabel("ARRAY SIZE")
    plt.ylabel("RUNNING TIME IN MS")
    for i, array in enumerate(test_results):
        plt.plot(x, array, color=np.random.rand(
            3, ), marker="o", label=f"Array #{i}")
    plt.show()
