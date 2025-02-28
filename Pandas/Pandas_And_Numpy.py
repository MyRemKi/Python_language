import pandas as pd
import numpy as np
import time as ts
import random as rand

class Map:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.np = 0
        self.pd = 0
        
    def Generate_Table_From_Numpy(self,randx,randy) :
        self.np = np.random.randint(randx,randy, size=(self.x,self.y))
        columns_list = []
        
        for i in range (self.y):
            columns_list.append(str(i))
        
        self.pd = pd.DataFrame(self.np,columns=columns_list)
    
    def Generate_Table_From_Dict(self,orient):
        random_dict = {rand.randint(1, 100): rand.randint(-100, 100) for _ in range(100)}
        if(orient=="yes"):
            self.pd = pd.DataFrame(random_dict,orient='index')
        
         else:
            self.pd = pd.DataFrame(random_dict)
    
    def Generate_Table_From_
    
    def Print(self):
        print(self.pd)
    
    def Return_Data_columns(self,columns):
        return self.pd[columns]
    
    def Return_Data_Row(self,row):
        print(self.pd.iloc[row])
        return self.pd.iloc[row]
        
    def Return_Data_Index_columns(self):
        return self.pd.columns
    
    def Return_Table_Type(self):
        return self.pd.dtypes
    
    def Define_Column_Data_Type(self,columnname,request):
        if(request=="int"):
            self.pd[columnname]= self.pd[columname].astype(int)
        
        if(request=="float"):
            self.pd[columnname]= self.pd[columname].astype(float)
        
        if(request=="string"):
            self.pd[columnname]= self.pd[columname].astype(str)

print('------------------------------------------')
map_1 = Map(100,100)
map_1.Initialize(-100,100)
map_1.Print()
print('------------------------------------------')
Loop=True
while Loop==True:
    request = str(input("$:"))
    if(request=="exit"):
        Loop=False
    if(request=="return -data=index"):
        print(map_1.Return_Data_Index_columns())
    
    if("return -data -col=" in request) :
        print(map_1.Return_Data_columns(request[18:]))
    
    if("return -data -row=" in request) :
        print(request[18:])
        print(Return_Data_Row(request[18:]))
