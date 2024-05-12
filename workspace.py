from threading import Thread
import time



done = False

def worker():
    counter=0
    while not done:
        time.sleep(1)
        counter+=1
        print(counter)

T1=Thread(target=worker)

T1.start() 
input("Press enter to quit") #wait user to input something
done = True


