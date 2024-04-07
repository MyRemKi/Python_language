import threading
import time

def TIME():
    sec=10
    for i in range (0,10):
        print(sec," sec")
        sec=sec-1
        time.sleep(1)

request=""

while(request != "exit"):
    request=str(input("$"))

    if(request=="time"):
        my_thread = threading.Thread(target=TIME)
        my_thread.start()
        my_thread.join()

    elif(request=="exit"):
        print("shuting down ...")
    else:
        print("invalid command !")
