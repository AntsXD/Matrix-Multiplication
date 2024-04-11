from time import perf_counter
import random
import numpy as np
from CppMatMult import fast_multiply

def multmat(A, B):
    if len(A[0]) == len(B):
        # Generate a list of 0 with rows of A and columns of B ( the zeros will be replaced)
        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        # x for rows in A
        for x in range(len(A)):
            # y for columns in B
            for y in range(len(B[0])):
                # z for rows in B
                for z in range(len(B)):
                    C[x][y] += A[x][z] * B[z][y]
            print('1 step done')

        return C

    else:
        return "Can't Calculate"

A = [[random.randint(1,100) for _ in range(500)] for _ in range(500)]
print("A Done")#making sure the matrix has been generated

start = perf_counter()
D = multmat(A, A)
print(D)
duration1 = perf_counter() - start


start = perf_counter()
C = fast_multiply(A,A)
print(C)
duration2 = perf_counter() -start


print(f"Time it took in py: {duration1} seconds")
print(f"Time it took in c++: {duration2} seconds")

if C == D:
    print("They are Exact!")
   


#500x500 took 111.75 sec in py    
#500x500 took 3.7 sec in Cpp   
#1000x1000 took 947.21 sec in py    
#1000x1000 took 34.3 sec in Cpp 
#2000x2000 took 6755.9 sec (112.5 mins) in py
#2000x2000 took 321.144sec (5.35 mins) in Cpp    
##more tests in doc  