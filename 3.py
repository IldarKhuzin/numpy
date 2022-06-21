# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.

import numpy as np

a = np.array([[1, 2, 3, 3, 1],[6, 8, 11, 10, 7]])
print(a)

mean_a = a.mean(axis=1)
print(mean_a)

a_centered = np.array([(a[0] - mean_a[0]),(a[1] - mean_a[1])])
print(a_centered)

print(a_centered[0][0])