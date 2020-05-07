import numpy as np

a11 = np.array([[1,2],[5,6]])
a12 = np.array([[3],[7]])
a21 = np.array([[9,12],[10,11]])
a22 = np.array([[13],[12]])

b11 = np.array([[1,2],[12,9]])
b12 = np.array([[3],[5]])
b21 = np.array([[10,11]])
b22 = np.array([[12]])

A = np.block([[a11,a12],[a21,a22]])
B = np.block([[b11,b12],[b21,b22]])

C = np.dot(A, B)

print(C)