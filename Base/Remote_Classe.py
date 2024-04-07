import math

class Point:

    def __init__(self,Name, X, Y):

        if (isinstance(Name, str)==False):

            print("Le parametre Name doit etre une chaine de caractere")
            exit("error name !")

        if (isinstance(X, int)==False or isinstance(Y, int)==False):

            print("Le parametre X et Y doit etre un entier")
            exit("error x,y !")

        self.name=str(Name)
        self.X=X
        self.Y=Y

    def ReturnName(self):
        return self.name

    def ReturnX(self):
        return self.X

    def ReturnY(self):
        return self.Y

    def __str__(self):
        #return "{}({},{}) / Type : Name {} ; X {} ; Y {}".format(self.name,self.X,self.Y,type(self.name),type(self.X),type(self.Y))
        return  "Point {} : ({},{})".format(point.ReturnName(),point.ReturnX(),point.ReturnY())


#Starting Here !!!

request=""
DictPoint={}

#Already Point Created

point=Point("A",0,0)
DictPoint[point.ReturnName()]=point
point=Point("B",0,2)
DictPoint[point.ReturnName()]=point
point=Point("C",-2,-2)
DictPoint[point.ReturnName()]=point


while(request != "exit"):
    request=str(input("$"))

    if(request=="create"):

        Name=str(input("Name : "))
        X=int(input("X : "))
        Y=int(input("Y : "))

        point=Point(Name,X,Y)

        DictPoint[point.ReturnName()]=point

    elif(request=="print"):

        for(c,v) in DictPoint.items():
            point=DictPoint[c]
            print(point)

    elif (request=="exit"):
        print("exiting...")

    elif (request=="remote"):

        PointOne=str(input("First point name : "))
        PointTwo=str(input("Second point name : "))

        if PointOne in DictPoint and PointTwo in DictPoint:

            PointOne=DictPoint[PointOne]
            PointTwo=DictPoint[PointTwo]

            distance = int(math.sqrt((PointTwo.ReturnX() - PointOne.ReturnX())**2 + (PointTwo.ReturnY() - PointOne.ReturnY())**2))

            print("The remote between the point {} and {} is around {}".format(PointOne.ReturnName(),PointTwo.ReturnName(),distance))

    else:
        print("invalid request")
