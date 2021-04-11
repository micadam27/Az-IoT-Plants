import time
import json
from datetime import datetime
import requests
import DeviceClient
import psutil
import socket

# START: Azure IoT Hub settings
KEY = "whDMFGt3ltHVf6w6iqd/Pdclgi67BIDInViITMV2s8I=";
HUB = "Mic-IOT-Hub";
DEVICE_NAME = str(hostname);
# END: Azure IoT Hub settings

#Connect device to Azure
device = DeviceClient.DeviceClient(HUB,DEVICE_NAME,KEY)
device.create_sas(600)

#TestData - Smaple
data = {}

#TestData - Get Computer Value
cpuusage = psutil.cpu_percent(4)
now = datetime.now()
timestamp = now.strftime("%H:%M")
hostname = str(socket.gethostname())


#TestData - Imput value in json
data["Name"] = str(hostname)
data["TimeStamp"] = str(timestamp)
data["CPU"] = float(cpuusage)

#Encode data to json
encoded_data = json.dumps(data,indent=1).encode('utf-8')

#Test json Output
print(device.send(encoded_data))
