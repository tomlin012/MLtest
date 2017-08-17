# encoding: utf-8
import numpy as np
import sys
A = np.genfromtxt(sys.argv[1],dtype='int')
B = np.genfromtxt(sys.argv[2],dtype='int')

"""
with open('matrixA.txt', encoding = 'UTF-8') as f:
    A = []
    for line in f:
        line = line.split() 
        if line:           
            line = [int(i) for i in line]
            A.append(line)
A = np.array(A)
"""


C = np.dot(A,B)

np.savetxt("ans_one.txt", C, fmt="%d", delimiter='\n') 


