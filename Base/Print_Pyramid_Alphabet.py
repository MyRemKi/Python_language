
list = "abcdefghijklmnopqrstuvwxyz" #Alphabet list

size_list=len(list)-1 #Take the size of the alphabet list
position=0 #Init the position of the alphabet list

for n in range (1,size_list+2):

    request=""

    for m in range (0,n):

        #If we're came the last position of the alphabet list
        if position > size_list :
            position=0

        request=request+list[position]
        position=position+1

    #Print the request (buiding pyramid)
    if(n<10):
        print(n,"  ",request)

    else:
        print(n," ",request)
