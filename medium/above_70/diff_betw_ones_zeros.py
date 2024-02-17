"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
"""
from typing import List


def ones_minus_zeros(grid: List[List[int]]) -> List[List[int]]:
    sum_r_1_0 = []
    sum_c_1_0 = []
    for _ in range(len(grid)):
        sum_r_1_0.append([0, 0])
    for _ in range(len(grid[0])):
        sum_c_1_0.append([0, 0])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                sum_r_1_0[i][0] += 1
                sum_c_1_0[j][0] += 1
            else:
                sum_r_1_0[i][1] += 1
                sum_c_1_0[j][1] += 1
    final = []
    for i in range(len(sum_r_1_0)):
        r = []
        for j in range(len(sum_c_1_0)):
            diff = sum_r_1_0[i][0] + sum_c_1_0[j][0] - sum_r_1_0[i][1] - sum_c_1_0[j][1]
            r.append(diff)
        final.append(r)
    return final


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 1, 1]]
    print(ones_minus_zeros(grid))
