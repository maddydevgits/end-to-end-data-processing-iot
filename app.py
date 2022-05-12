from physicalLayer import *
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
from flask import Flask,request,redirect,render_template
import json
app=Flask(__name__)
k=''

# create a client object
client=AWSIoTMQTTClient('5aSACET_client1')

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

@app.route('/sensorydata',methods=['GET','POST'])
def sensoryData():
    global k
    d=k.decode('utf-8')
    d=json.loads(d)
    print(d['Humidity'])
    return render_template('index.html',hum_data=d['Humidity'],temp_data=d['Temperature'],rain_data=d['Rainfall'])

def notification(client,userdata,message):
    global k
    print(message.payload)
    k=message.payload

client.connect() # connect with AWS with all above credentials
print('AWS Connected')
time.sleep(2)

client.subscribe('SACET/5a',1,notification)

if __name__=="__main__":
    app.run(debug=True)