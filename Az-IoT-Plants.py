import time
import json
from datetime import datetime
import requests
import DeviceClient
import psutils
import socket
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

hostname = str(socket.gethostname())

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

# START: Azure IoT Hub settings
KEY = "whDMFGt3ltHVf6w6iqd/Pdclgi67BIDInViITMV2s8I=";
HUB = "Mic-IOT-Hub";
DEVICE_NAME = str(hostname);
# END: Azure IoT Hub settings

#Connect device to Azure
device = DeviceClient.DeviceClient(HUB,DEVICE_NAME,KEY)
device.create_sas(600)

#Sample
data = {}

# read moisture level through capacitive touch pad
touch = ss.moisture_read()

# read temperature from the temperature sensor
temp = ss.get_temp()

#Get Computer Value
cpuusage = psutil.cpu_percent(4)
now = datetime.now()
timestamp = now.strftime("%H:%M")
memusage = psutil.virtual_memory().percent

#Imput value in json
data["Name"] = str(hostname)
data["TimeStamp"] = str(timestamp)
data["CPU"] = float(cpuusage)
data["Memory"] = float(memusage)
data["Soil Temp"] = str(temp)
data["moisture"] = str(touch)

#Encode data to json
encoded_data = json.dumps(data,indent=1).encode('utf-8')

#Test json Output
print(device.send(encoded_data))

print("temp: " + str(temp) + "  moisture: " + str(touch))
