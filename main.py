from physicalLayer import *
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

# create a client object
client=AWSIoTMQTTClient('5aSACET_client')

# configure the aws endpoint
client.configureEndpoint('a366shaagepcsd-ats.iot.eu-west-1.amazonaws.com',8883)

# configure the credentials -> root certificate, device private key,device certificate 
client.configureCredentials('AmazonRootCA1.pem','device-private.pem.key','device-certificate.pem.crt')

#configure the publishing queue
client.configureOfflinePublishQueueing(-1) # infinite publishing

#configure the draining frequency
client.configureDrainingFrequency(2) # frequency of data transfer 

# configure the timeout - connect disconnect
client.configureConnectDisconnectTimeout(10) # 10ms 

# configure operation timeout
client.configureMQTTOperationTimeout(5) # 5ms

client.connect() # connect with AWS with all above credentials
print('AWS Connected')
time.sleep(2)

while True:
    dataStream=str(collectData())
    print(dataStream)
    client.publish('SACET/5a',dataStream,0) #topic, our message
    time.sleep(2) # 2 seconds