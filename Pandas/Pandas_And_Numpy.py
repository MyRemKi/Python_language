import pandas as pd
import numpy as np
import time as ts
import random as rand

class Map:
    
    def __init__(self,x,y):
        self.size_x = x
        self.size_y = y
        self.np = 0
        self.pd = 0
        
    def Generate_Table_From_Numpy(self,randx,randy) :
        self.np = np.random.randint(randx,randy, size=(self.size_x,self.size_y))
        columns_list = []
        
        for i in range (self.size_y):
            columns_list.append(str(i))
        
        self.pd = pd.DataFrame(self.np,columns=columns_list)
    
    def Generate_Table_From_Dict(self,orient):
        random_dict = {rand.randint(1, 100): rand.randint(-100, 100) for _ in range(100)}
        if(orient=="yes"):
            self.pd = pd.DataFrame.from_dict(random_dict,orient='index')
        else:
            self.pd = pd.DataFrame(random_dict)
    
    def Generate_Table_From_File(self,name,chardelimiter=''):
        if(chardelimiter!=''):
            self.pd = pd.DataFrame.read_csv(name, delimiter=chardelimiter)
        else:
            self.pd = pd.DataFrame.read_csv(name)
        
    
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
map_1.Print()
print('------------------------------------------')
Loop=True
while Loop==True:
    request = str(input("$:"))
    if(request=="exit"):
        Loop=False
    
    elif("setDataFrame" in request):
        
        if("-dict" in request[12:]):
            request=str(input("orient ? (yes/no) ->"))
            map_1.Generate_Table_From_Dict(self,request)
            
        elif("-numpy" in request[12:]):
            Size=[]
            request=int(input("Minimum Number ... ->"))
            Size.append(request)
            request=int(input("Maximum Number ... ->"))
            Size.append(request)
            map_1.Generate_Table_From_Numpy(Size[0],Size[1])
            
        elif("-file" in request[12:]):
            if("csv" in request[17:]):
                request=str(input("name of file ... ->"))
                map_1.Generate_Table_From_File()
            elif("txt" in request[17:]):
                Data=[]
                request=str(input("name of file ... ->"))
                Data.append(request)
                request=str(input("delimiter ... ->"))
                Data.append(request)
                map_1.Generate_Table_From_File(Data[0],Data[1])
                
                
    elif(request=="return -data=index"):
        print(map_1.Return_Data_Index_columns())
    
    elif("return -data -col=" in request) :
        print(map_1.Return_Data_columns(request[18:]))
    
    elif("return -data -row=" in request) :
        print(request[18:])
        print(Return_Data_Row(request[18:]))
