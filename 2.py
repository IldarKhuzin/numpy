# Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков,
# содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен
# иметь размер 5x2.

import numpy as np

a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]])
print(a)
mean_a = a.mean(axis=0)
print(mean_a)

a_centered = np.array([(a[:,0] - mean_a[0]),(a[:,1] - mean_a[1])]).transpose()
print(a_centered)
