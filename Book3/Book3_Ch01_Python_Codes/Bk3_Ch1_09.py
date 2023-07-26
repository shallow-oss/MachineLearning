
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch1_09

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

A_first_col = A[:, 0]  # saved as one dimension row
print(A_first_col)
A_first_col_V2 = A[:, [0]]  # saved as a column
print(A_first_col_V2)
A_first_second_col_V2 = A[:, [0, 1]]  # extract first and second columns
print(A_first_second_col_V2)
A_first_third_col_V2 = A[:, [0, 2]]  # extract first and third columns
print(A_first_third_col_V2)
A_first_row = A[[0], :]  # extract first row
print(A_first_row)
A_second_row = A[[1], :]  # extract second row
print(A_second_row)
A_second_row_first_col = A[[1], [0]]  # i = 2, j = 1
print(A_second_row_first_col)
