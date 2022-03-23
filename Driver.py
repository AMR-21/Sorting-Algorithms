# NOTE:  Picking the Sizes of arrays and the how many arrays used at each size
import random
import Visualizer
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

    Test = Visualizer.tester()
    Test.selector(TestArrays, WhichAlgos,ValueOfSamples)
