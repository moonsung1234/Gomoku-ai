from table import Tool
from play import ControlTemplate
import numpy as np
import random as rd

tool = Tool()
con = ControlTemplate()

v_table = []
tables = []

table = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])

GAMMA = 0.1
WIN = 1
LOSE = -3
DRAW = -1
turned = 1

for _ in range(3) :  
    table = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])

    while(True) :
        extracted_table = tool.extractTable(table, 0)
        index_table = tool.searchTable(tables, extracted_table, table, 0)
        is_exist, table_index = tool.findTable(tables, table)
        point_table = []
        index_list = None

        for it in index_table :
            point_table.append((it[0], table_index, it[1]))

        if not len(index_table) == 0 :
            random_int = con.chooseByEgreedy()

            if random_int :
                print("find : ", index_table)
                max_it0, max_it1 = point_table[0][0], point_table[0][2]

                if is_exist :
                    for pt in point_table :
                        if v_table[pt[1]] >= v_table[table_index] :
                            max_it0, max_it1 = pt[0], pt[2]

                    error = v_table[max_it0] + GAMMA * v_table[max_it0] - v_table[table_index]
                    v_table[table_index] =  round(GAMMA * error, 3)
                    
                else :
                    tables.append(table.copy())
                    v_table.append(random_next_v)
                    tmp_index = len(v_table) - 1

                    error = v_table[max_it0] + GAMMA * v_table[max_it0] - v_table[tmp_index]
                    v_table[tmp_index] = round(GAMMA * error, 3)
                    
                table[max_it1[0], max_it1[1]] = turned
                index_list = max_it1

            else :
                print("fail random")
                idx1, idx2 = con.getRandomIndex(table, 0)    
                random_next_v = round(-1 * rd.random(), 3)
                
                if is_exist :
                    error = random_next_v + GAMMA * random_next_v - v_table[table_index]
                    v_table[table_index] =  round(GAMMA * error, 3)
                    
                else :
                    tables.append(table.copy())
                    v_table.append(random_next_v)

                table[idx1, idx2] = turned
                index_list = (idx1, idx2)

        else :
            print("random")
            idx1, idx2 = con.getRandomIndex(table, 0)    
            random_next_v = round(-1 * rd.random(), 3)

            if is_exist :
                error = random_next_v + GAMMA * random_next_v - v_table[table_index]
                v_table[table_index] =  round(GAMMA * error, 3)
                
            else :
                tables.append(table.copy())
                v_table.append(random_next_v)

            table[idx1, idx2] = turned
            index_list = (idx1, idx2)

        result = con.checkGameState(table, 0, turned, [index_list[0], index_list[1]])
        print(table)

        if result == WIN :
            print(turned, " 승리")
            turned = 2 if turned == 1 else 1

            break

        elif result == DRAW :
            print("무승부")
            turned = 2 if turned == 1 else 1

            break

        turned = 2 if turned == 1 else 1

print(tables)
print(v_table)