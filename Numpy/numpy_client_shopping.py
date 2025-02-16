import numpy as np
import random

#Return the shopping client can made from random.
def store_product():
    rand1 = random.randint(1000,2500)
    list = []
    for i in range(rand1):
        rand2 = int(random.randint(10000,99999))
        list.append([i,rand2])

    product = np.array(list, dtype='int32')

    return product

#Return the shopping client can made by the code item as input (all information).
def define_product(code):
    print("product :",code)
    list_product = {1 : "soft/beer", 2 : "deli shop/item", 3 : "baker's shop/item", 4 : "cheese shop/item", 5 : "fruits/vegetables", 6 : "clothes", 7 : "home material/furniture item", 8 : "IT materials/item", 9 : "DIY item"}

    data = int(code/10000)
    print("data by product code :",data)
    data = list_product[data]

    return "protuct type : "+data

#Return the shopping client made by the code item as input.
def define_product_all_and_copy(array,size):
    list_product = {1 : "soft/beer", 2 : "deli shop/item", 3 : "baker's shop/item", 4 : "cheese shop/item", 5 : "fruits/vegetables", 6 : "clothes", 7 : "home material/furniture item", 8 : "IT materials/item", 9 : "DIY item"}
    list = []

    for i in range(0,int((array.size/2))):
        data = array[i,1]
        data1 = int(data/10000)
        list.append([i,data1])

    product = np.array(list, dtype='int32')
    return product

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
client = store_product()
print("Client made shopping : \n",client)

print("---------------------------------------------------------------------------")
rand = int(random.randint(0,client.size-1)/2)
if(client[rand,0] == rand):
    rand = client[rand,1]
print(define_product(rand))

print("---------------------------------------------------------------------------")
print(define_product_all_and_copy(client,client.size-1))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

class Product:

    def __init__(self):
        self.list = {1 : "soft/beer", 2 : "deli shop/item", 3 : "baker's shop/item", 4 : "cheese shop/item", 5 : "fruits/vegetables", 6 : "clothes", 7 : "home material/furniture item", 8 : "IT materials/item", 9 : "DIY item"}
        self.min_code_product = 10000
        self.max_code_product = 99999

    def store_product(self,min_shopping,max_shopping):
        rand1 = random.randint(min_shopping,max_shopping)
        list = []

        for i in range(rand1):
            rand2 = int(random.randint(self.min_code_product,self.max_code_product))
            list.append([i,rand2])

        product = np.array(list, dtype='int32')

        return product

    def define_product_all_and_copy(self,array):

        for i in range(0,int((array.size/2))):
            data = array[i,1]
            data1 = int(data/self.min_code_product)
            list.append([i,data1])

        product = np.array(list, dtype='int32')
        return product

    def define_product(self,code):
        print("product :",code)

        data = int(code/self.min_code_product)
        print("data by product code :",data)

        data = self.list[data]
        return "protuct type : "+data

    def define_product_type(self,array):
        product = []

        for i in range(0,int((array.size/2))):
            data1 = array[i,1]
            data2 = int(data1/self.min_code_product)
            data3 = [i,array[i,1],self.list[data2]]
            product.append(data3)

        return product

    def print_product(self,array):
        size_name = 0
        size_number = 0

        for i in array:
            if(size_name < len(i[2])):
                size_name = len(i[2])

            if(size_number < len(str(i[0]))):
                size_number = len(str(i[0]))


        for i in array:
            print("item n°{}{} : {}{} | product n°{}".format(i[0],(size_number - len(str(i[0])))*" ",i[2],(size_name - len(i[2]))*" ",i[1]))

#Assign the "Product" class to the prod variable.
prod = Product()

#Declare client variable as vector numpy like min and max shopping client can make by "Product" class function.
min_shopping = 1000
max_shopping = 2500
client = prod.store_product(min_shopping,max_shopping)

#Assign the result for the function "define_product_type" to the same variable assigned as a vector made from numpy.
client = prod.define_product_type(client)

#Show the shopping list the client made.
prod.print_product(client)

