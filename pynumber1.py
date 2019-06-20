import numpy as np
r=int(input("Enter the no. of rows:"))
c=int(input("Enter the no. of columns"))
if r==6 and c==7:
   arr=np.random.randint(100,size=(r,c))
elif r==3 and c==2:
    arr=np.random.randint(100,size=(r,c))
else:
     print("Please enter the rxc in the form of 3x2 and 6x7")
print(arr)
    
np.save("2D_array.txt",arr)
