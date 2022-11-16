import datetime
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()


start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=600)

with open ("test.csv", "w") as file:
    file.write("Time , Temperature , Pressure, Humidity \n")

while now_time < start_time + duration:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    now_time= datetime.datetime.now()

    with open ("test.csv", "a") as file:
        file.write("%s, %s, %s, %s \n" % (now_time, t,p,h))
    sleep(60)

if now_time > start_time + duration:
    print("done")
    
    
