# encoding: utf-8
import numpy as np

A = np.genfromtxt('matrixA.txt',dtype='int')
B = np.genfromtxt('matrixB.txt',dtype='int')

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

np.savetxt("ans.txt", C, fmt="%d", delimiter='\n') 


