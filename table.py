import numpy as np
import random as rd

class Tool :
    def extractTable(self, np_table, init_value) :
        index_table = []

        for i in range(len(np_table)) :
            for j in range(len(np_table[0])) :
                if not np_table[i, j] == init_value :
                    index_table.append([i, j])

        if len(index_table) == 0 :
            return np_table

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


    def searchTable(self, np_tables, target_table, origin_table, init_value) :
        returned_array = []

        for ti in range(len(np_tables)) :
            parent_table = np_tables[ti].tolist()
            child_table = target_table.tolist()

            all_count1 = 0
            all_count2 = 0

            for check_i in range(len(parent_table)) :
                for check_j in range(len(parent_table[0])) :
                    if not parent_table[check_i][check_j] == init_value :
                        all_count1 += 1

            for check_i in range(len(child_table)) :
                for check_j in range(len(child_table[0])) :
                    if not child_table[check_i][check_j] == init_value :
                        all_count2 += 1

            for i in range(len(parent_table)) :
                if i > (len(parent_table) - 1) - (len(child_table) - 1) :
                    break

                is_break = False

                for j in range(len(parent_table[0])) :
                    if j > (len(parent_table[0]) - 1) - (len(child_table[0]) - 1) :
                        break

                    wrong_count = 0
                    wrong_index = None

                    for ii in range(i, i + len(child_table)) :
                        for jj in range(j, j + len(child_table[0])) :
                            if not parent_table[ii][jj] == child_table[ii - i][jj - j] :
                                wrong_count += 1
                                wrong_index = (ii, jj)

                    for check_i in range(len(parent_table)) :
                        for check_j in range(len(parent_table[0])) :
                            if not i <= check_i <= i + len(child_table) - 1 or not j <= check_j <= j + len(child_table[0]) - 1 :
                                if not parent_table[check_i][check_j] == init_value :
                                    wrong_count += 1
                                    wrong_index = (check_i, check_j)

                    if wrong_count == 1 and all_count1 > all_count2 :
                        if origin_table[wrong_index[0], wrong_index[1]] == init_value :
                            returned_array.append((ti, wrong_index))
                            is_break = True
                            break

                if is_break :
                    break

        return returned_array

    def findTable(self, tables, target_table) :
        for t_i in range(len(tables)) :
            result_table = tables[t_i] == target_table

            for i in range(len(result_table)) :
                for j in range(len(result_table[0])) :
                    if not result_table[i, j] :
                        break

                if not result_table[i, j] :
                    break

                elif i == len(result_table) - 1 and j == len(result_table[0]) - 1 :
                    return True, t_i

        return False, None
            