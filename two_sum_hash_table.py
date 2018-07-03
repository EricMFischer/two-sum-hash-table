'''
The goal of this problem is to implement a variant of the 2-SUM algorithm. The file contains 1
million integers, both positive and negative (there might be some repetitions). The ith row of
the file specifies the ith entry of the array.

The task is to compute the number of target values t in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x and y in the input file that satisfy x + y = t. (NOTE:
ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for
it. For example, you could compare performance under the chaining and open addressing approaches
to resolving collisions.
'''
from multiprocessing import Pool
import time

# Global variables
H = {}


# input: target value
def find_two_sum(t_val):
    global T_VALS
    for num in H:
        if t_val - num in H:
            return 1
    return 0


# input: filename, interval
# output: number of target values t in interval such that x + y = t, where x and y are distinct
# numbers in input file
def two_sum(filename, i):
    global H
    with open(filename) as f_handle:
        for line in f_handle:
            H[int(line)] = 1

    pool = Pool()
    result = pool.map(find_two_sum, list(range(i[0], i[1] + 1)))
    return sum(result)


def main():
    start = time.time()

    interval = [-10000, 10000]
    # interval = [3, 1000000]
    result = two_sum('two_sum_hash_table.txt', interval)

    print('result: ', result)
    print('elapsed time: ', time.time() - start)


main()
