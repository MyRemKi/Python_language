import pandas as pd
import numpy as np
import time as ts

class Map:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.np = 0
        self.pd = 0
        
    def Initialize(self,randx,randy) :
        self.np = np.random.randint(randx,randy, size=(self.x,self.y))
        columns_list = []
        
        for i in range (self.y):
            columns_list.append(str(i))
        
        self.pd = pd.DataFrame(self.np,columns=columns_list)
        
    def Print(self):
        print(self.pd)
    
    def Return_Data_columns(self):
        return self.pd.columns
    
    def Return_Data_Index_columns(self):
        return self.pd.columns

print('------------------------------------------')
map_1 = Map(100,100)
map_1.Initialize(-100,100)
map_1.Print()
print('------------------------------------------')
LoopCount=10
while LoopCount!=0:
    request = str(input("$:"))
    if(request=="exit"):
        LoopCount=0
    if(request=="return -col"):
        print(map_1.Return_Data_columns())
    
