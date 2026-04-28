from mosip_auth_sdk.models import DemographicsModel
from mosip_auth_sdk import MOSIPAuthenticator
from dynaconf import Dynaconf
import serial

config = Dynaconf(settings_files=["./config.toml"], environments=False)
authenticator = MOSIPAuthenticator(config=config)

arduino = serial.Serial("COM9", 115200, timeout=.1) 

while True: 
        data = arduino.readline() 
        print(data) # printing the value 
