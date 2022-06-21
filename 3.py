# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.

import numpy as np

N = 5 # число наблюдений

a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]])
print(a)
mean_a = a.mean(axis=0)
print(mean_a)

a_centered = np.array([(a[:,0] - mean_a[0]),(a[:,1] - mean_a[1])]).transpose()
print(a_centered)

a_centered_sp = np.dot(a_centered[:,0], a_centered[:,1])
print(f'ковариация двух признаков массива а - {a_centered_sp / (N - 1)}')

