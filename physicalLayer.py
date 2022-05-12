import random
import time

def collectData():
    print('Collecting Data from Device')
    h=random.randint(20,100)  # h - humidity
    t=random.randint(20,50)   # t- temperature
    r=random.randint(100,300) # r- rainfall
    time.sleep(4) # 4 seconds delay
    data='{"Humidity":'+str(h)+',"Temperature":'+str(t)+',"Rainfall":'+str(r)+'}'
    return data