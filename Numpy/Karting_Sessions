import numpy as np
import random as rd

class Karting_Session:
    def __init__(self):
        self.list=[]
        self.besttime=0
    
    def Make_Session(self):
        self.list = np.random.uniform(0.48,1.20, size=(3,5))
        self.list = np.round(self.list, 2)
        self.besttime= np.min(self.list)
    
    def Return_Data_Session(self):
        return self.list
    
    def __str__(self):
        return "Session : \n" + str(self.list) + "\n Best Time made : " + str(self.besttime) + "s"
    
session_1 = Karting_Session()
session_1.Make_Session()
print(session_1.__str__())
