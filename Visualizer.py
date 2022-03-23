import timeit
import Algorithms
import matplotlib.pyplot as plt
import numpy as np

# FIXME: While running you will notice that the compiler returns cannnot import TestArrays look line 13 for refrence
#       but without this line it will see test_arrays as a non defined variable
#       upon fixing this it should be able to work


class tester:

    def selector(self, test_arrays, which_algo, value_of_samples):

        test_results = [[], [], [], [], []]
        SETUP_CODE = '''import timeit, Algorithms\nfrom Driver import TestArrays'''

        for i in range(len(which_algo)):

            if which_algo[i] == 0:
                TEST_CODE = '''j=0\nfor j in range(len(test_arrays)):\n\ttest = Algorithms.QuickSort()\ntest.quicksort(test_arrays[j])'''
                times = timeit.repeat(
                    setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
                test_results[i].append(min(times))

            elif which_algo[i] == 1:
                TEST_CODE = '''j=0\nfor j in range(len(test_arrays)):\n\ttest = Algorithms.MergeSort()\ntest.mergesort(test_arrays[j])'''
                times = timeit.repeat(
                    setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
                test_results[i].append(min(times))

            elif which_algo[i] == 2:
                TEST_CODE = '''j=0\nfor j in range(len(test_arrays)):\n\ttest = Algorithms.SelectionSort()\ntest.SelectionSort(test_arrays[j])'''
                times = timeit.repeat(
                    setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
                test_results[i].append(min(times))

            elif which_algo[i] == 3:
                TEST_CODE = '''j=0\nfor j in range(len(test_arrays)):\n\ttest = Algorithms.InsertionSort()\ntest.insertionsort(test_arrays[j])'''
                times = timeit.repeat(
                    setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
                test_results[i].append(min(times))

            elif which_algo[i] == 4:
                TEST_CODE = '''j=0\nfor j in range(len(test_arrays)):\n\ttest = Algorithms.HybridSort()\ntest.hybridsort(test_arrays[j])'''
                times = timeit.repeat(
                    setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
                test_results[i].append(min(times))

        Visualizer.display(test_results, value_of_samples)


class Visualizer:
    def display(self, test_results, value_of_samples):
        plt.title("Running Times")
        x = value_of_samples
        plt.xlabel("ARRAY SIZE")
        plt.ylabel("RUNNING TIME IN MS")
        for i, array in enumerate(test_results):
            plt.plot(x, array, color=np.random.rand(
                3, ), marker="o", label=f"Array #{i}")
        plt.show()
