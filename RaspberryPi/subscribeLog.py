import paho.mqtt.client as mqtt #import the client1
from datetime import datetime
import os


###########################################
### Global variables
###########################################
broker_address="192.168.0.129"
topic = 'SENS-1'



###########################################
### Create csv  file with column titles
###########################################
if os.path.isfile("test.csv") != True:
	file = open('test.csv','a')
	file.write('Date,Time,Temperature,Humidity')
	file.write("\n")
	file.close()
###########################################
### Callback function 
###Writes to csv file everytime we receive data from sensor.
###########################################
def on_message(client, userdata, message):
	now = datetime.today()
	timestamp = now.strftime("%Y-%m-%d,%H:%M:%S")
	log = timestamp + "," + str(message.payload.decode("utf-8")) + "\n"
	print("Message received: " + log)
	file = open('test.csv','a')
	file.write(log)
	file.close()
########################################

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic",topic)
client.subscribe(topic)
client.loop_forever() #start the loop