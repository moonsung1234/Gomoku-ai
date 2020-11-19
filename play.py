import numpy as np
import random as rd

class ControlTemplate :
    def chooseByEgreedy(self) :
        return rd.choices(range(0, 2), weights=[40, 60])[0]

    def getRandomIndex(self, np_table, init_value) :
        length = 0
        score_index = None
        weights_array = []

        for i in range(len(np_table)) :
            for j in range(len(np_table[0])) :
                if not np_table[i, j] == init_value and score_index == None :
                    score_index = (i, j)

                length += 1

        for i in range(len(np_table)) :
            for j in range(len(np_table[0])) :
                if score_index == None :
                    weights_array.append(1)

                else :
                    weights_array.append(self.getPercentageBaseWeights(score_index, (i, j)))

        random_index = rd.choices(range(0, length), weights=weights_array)[0]
        y1, x1 = self.setTwoDimensionalIndex(np_table, random_index)
        
        while True :
            if not np_table[y1, x1] == init_value :
                random_index = rd.choices(range(0, length), weights=weights_array)[0]
                y1, x1 = self.setTwoDimensionalIndex(np_table, random_index)
        
            else :
                break

        return y1, x1

    def getPercentageBaseWeights(self, goal_index, target_index) :
        difference = abs(goal_index[0] - target_index[0]) + abs(goal_index[1] - target_index[1]) 

        if difference <= 2 :
            return 30

        elif difference <= 5 :
            return 10

        elif difference <= 8 :
            return 5

        else :
            return 1

    def setTwoDimensionalIndex(self, np_table, index) :
        tmp_num = index
        i, j = 0, index
        length = 0

        for _ in range(len(np_table[0])) :
            length += 1

        while tmp_num >= length :
            tmp_num -= length
            i += 1
            j -= length

        return i, j

    def checkGameState(self, np_table, init_value, turned, index) :
        #가로 검사
        for i in range(len(np_table[0]) - 4) :
            for j in range(5) :
                if not np_table[index[0], i + j] == turned :
                    break

                elif j == 4 :
                    return 1

        #세로검사
        for i in range(len(np_table) - 4) :
            for j in range(5) :
                if not np_table[i + j, index[1]] == turned :
                    break

                elif j == 4 :
                    return 1

        #대각선 검사(왼쪽 위 -> 오른쪽 아래)
        standard_index = index
        
        while(True) :
            if standard_index[0] - 1 < 0 or standard_index[1] - 1 < 0 :
                break

            standard_index[0] -= 1
            standard_index[1] -= 1

        while(True) :
            if standard_index[0] + 4 > len(np_table) - 1 or standard_index[1] + 4 > len(np_table[0]) - 1 :
                break

            for i in range(5) :
                if not np_table[standard_index[0] + i, standard_index[1] + i] == turned :
                    break

                elif i == 4 :
                    return 1 

            standard_index[0] += 1
            standard_index[1] += 1

        #대각선 검사(오른쪽 위 -> 왼쪽 아래)
        standard_index = index
        
        while(True) :
            if standard_index[0] - 1 < 0 or standard_index[1] + 1 > len(np_table[0]) - 1 :
                break

            standard_index[0] -= 1
            standard_index[1] += 1

        while(True) :
            if standard_index[0] + 4 > len(np_table) - 1 or standard_index[1] - 4 < 0 :
                break

            for i in range(5) :
                if not np_table[standard_index[0] + i, standard_index[1] - i] == turned :
                    break

                elif i == 4 :
                    return 1

            standard_index[0] += 1
            standard_index[1] -= 1

        #무승부인지 검사
        for i in range(len(np_table)) :
            for j in range(len(np_table[0])) :
                if np_table[i, j] == init_value :
                    break

            if np_table[i, j] == init_value :
                    break

            elif i == len(np_table) - 1 and j == len(np_table[0]) - 1:
                return -1
            