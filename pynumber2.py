import numpy as np
row_list=[]
col_list=[[]]
for i in range(8):
  for j in range(2):
    row_list.append(np.random.randint(100,195))
    row_list.append(row_list[0]+5)
    col_list.append([row_list]) 
