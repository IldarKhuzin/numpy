# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.

import numpy as np

N = 2 # число наблюдений

a = np.array([[1, 2, 3, 3, 1],[6, 8, 11, 10, 7]])
mean_a = a.mean(axis=1)
a_centered = np.array([(a[0] - mean_a[0]),(a[1] - mean_a[1])])

a_centered_sp = np.dot(a_centered[0], a_centered[1])
print(f'ковариация двух признаков массива а - {a_centered_sp / (N - 1)}')
