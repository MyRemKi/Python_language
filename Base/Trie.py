import random

def Trie_Croissant(Table): #Trie par insertion
    n= len(Table)
    for x in range (1,n):
        i =Table[x]
        y=x-1
        while (y>=0 and Table[y]>i) :
            Table[y+1]=Table[y]
            y=y-1
            Table[y+1]=i

    return Table

def Trie_Decroissant(Table): #Trie par selection
    for x in range(len(Table)):
        i = x
        for y in range(x+1, len(Table)):
            if (Table[i] <Table[y]):
                i = y

        j = Table[x]
        Table[x] = Table[i]
        Table[i] = j

    return Table

def Trie_Pair_Impair(Table): #Trie par Insertion pour chiffre Pair et Selection pour chiffre Impair
    Pair=[]
    Impair=[]
    for x in Table:
        if(x%2 == 0):
            Pair.append(x)
        else:
            Impair.append(x)

    Pair=Trie_Croissant(Pair)
    Impair=Trie_Decroissant(Impair)
    Table=Pair+Impair

    return Table

def Generate_Number_Alea(Table,N,Min,Max): #Genere aleatoirement des nombres

    for x in range (0,N):
        Table.append(random.randint(Min,Max))

    return Table

def Create_List():
    return []


table=[]
request =""
boucle=1

while(request!="exit"):

    print("_____________ ",boucle," _____________")
    request = str(input())

    if(request.find("create")!=-1):

        table=Create_List()

    elif(request.find("generate") != -1 and request.find("generate")<1):

        if(table==[]):

            if(request.find("-q")!=-1):

                if(request.find("-min")!=-1 and request.find("-max")!=-1):

                    rqt=request.find("-q")+2
                    rqt=request[rqt:(request.find("-min"))]
                    N=int(rqt.strip())


                    rqt=request.find("-min")+4
                    rqt=request[rqt:(request.find("-max"))]
                    Min=int(rqt.strip())

                    rqt=request.find("-max")+4
                    rqt=request[rqt:]
                    Max=int(rqt.strip())

                else:

                    rqt=request.find("-q")+2
                    rqt=request[rqt:len(request)]
                    N=int(rqt.strip())
                    Min=1
                    Max=6

            elif(request.find("-min")!=-1 and request.find("-max")!=-1):

                N=1

                rqt=request.find("-min")+4
                rqt=request[rqt:(request.find("-max"))]
                print("request :",rqt)
                Min=int(rqt.strip())
                print("Min :",Min)

                rqt=request.find("-max")+4
                rqt=request[rqt:]
                print("request :",rqt)
                Max=int(rqt.strip())
                print("Max :",Max)

            elif(request.find("-q")<request.find("-min") or request.find("-q")<request.find("-max") or request.find("-min")<request.find("-max")):

                print("invalid command")
                N=0
                Min=0
                Max=0

            else:

                N=1
                Min=1
                Max=6

            table=Generate_Number_Alea(table,N,Min,Max)

        else:

            print("your list isn't empty ...")
            print("enter 'create' to generate a new empty list")

    elif(request=="print"):

        print(table)

    elif(request=="exit"):

        break;

    elif(request.find("classify")!=-1):

        if(table!=[]):

            if(request.find("-pi")!=-1):

                table=Trie_Pair_Impair(table)

            elif(request.find("-tc")!=-1):

                table=Trie_Croissant(table)

            elif(request.find("td")!=-1):

                table=Trie_Decroissant(table)

            else:

                print("invalid command")

        else:

            print("Your list is empty or get only 1 number ...")
            print("EMPTY---")
            print("If it's empty ... enter 'generate -q (quantity bigger than or equal 2)' to classify the list")
            print("ONLY 1---")
            print("If there is only 1 number ... enter 'create' to generate a new empty list")
            print("And then you enter 'generate -q (quantity bigger than or equal 2)' to classify the list")

    else:

        print("invalid command")

    boucle=boucle+1

