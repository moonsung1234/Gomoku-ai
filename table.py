import numpy as np
import random as rd

class Tool :
    def extractTable(self, np_table, init_value) :
        index_table = []

        for i in range(len(np_table)) :
            for j in range(len(np_table[0])) :
                if not np_table[i, j] == init_value :
                    index_table.append([i, j])

        index_table = np.array(index_table)
        sliced_table1 = index_table[:, 0:1]
        sliced_table2 = index_table[:, 1:]
 
        y1, x1 = np.min(sliced_table1), np.min(sliced_table2)
        y2, x2 = np.max(sliced_table1), np.max(sliced_table2)
        returned_table = np.array([
            [0 for zero in range(x2 - x1 + 1)] for t in range(y2 - y1 + 1)
        ])

        for i in range(y1, y2 + 1) :
            for j in range(x1, x2 + 1) :
                returned_table[i - y1, j - x1] = np_table[i, j]

        return returned_table


    def searchTable(self, np_table, target_table) :
        parent_table = np_table.tolist()
        child_table = target_table.tolist()

        for i in range(len(parent_table)) :
            if i > (len(parent_table) - 1) - (len(child_table) - 1) :
                break

            for j in range(len(parent_table[0])) :
                if j > (len(parent_table[0]) - 1) - (len(child_table[0]) - 1) :
                    break

                print((i, j))

                for ii in range(i, i + len(child_table)) :
                    for jj in range(j, j + len(child_table[0])) :
                        if not parent_table[ii][jj] == child_table[ii - i][jj - j] :
                            break

                    if not parent_table[ii][jj] == child_table[ii - i][jj - j] :
                        break

                    elif ii == i + len(child_table) - 1 :
                        return True

        return False
            