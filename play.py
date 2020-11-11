import numpy as np
import random as rd

class ControlTemplate :
    def getRandomIndex(self, np_table, init_value) :
        length = 0

        for i in range(len(np_table)) :
            for j in range(len(np_table[0])) :
                length += 1
 
        y1, x1 = self.setTwoDimensionalIndex(np_table, rd.randint(0, length - 1))
        
        while True :
            if not np_table[y1, x1] == init_value :
                y1, x1 = self.setTwoDimensionalIndex(np_table, rd.randint(0, length - 1))
        
            else :
                break

        return y1, x1

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
        
