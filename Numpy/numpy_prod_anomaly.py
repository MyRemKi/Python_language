import numpy as np
import random
import time as ts

def init_production():
    prod = np.random.randint(0,5,size=(3,3), dtype='int8')

    ral = tuple(random.randint(0,2) for _ in range(2)) #random_anomaly_location
    prod[ral[0],ral[1]]=-1
    return prod

def IsAnomaly(array):
    Check = array>=0
    if(np.any(Check==False)):
        return True
    else:
        return False


def find_anomaly(array):
    Check = array>=0
    Location = np.where(Check == False)
    Location = tuple(zip(Location[0],Location[1]))
    return Location

mat = init_production()

if(IsAnomaly(mat)):
    print("There is an anomaly")
    Location = find_anomaly(mat)

    print("--------------------")
    print("prod : \n",mat)
    print("---anomaly--found---")
    print(Location)
else:
    print("Everything is okay")

