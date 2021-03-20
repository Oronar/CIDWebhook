import serial
import requests
import re
import configparser
import os
from CallerId import CallerId

def pushNotification(title, message, prioriy = 5):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
    return requests.post(config["APP"]["WEBHOOK"], json = {
            "message": message,
            "title": title,
            "priority": 5
    })

def parseData(data):
    regResult = re.findall("(....) = (.*)", data)
    if(len(regResult) == 0):
        return

    caller = CallerId.getInstance()
    if(regResult[0][0] == "DATE"):
        caller.Date = regResult[0][1]
    
    if(regResult[0][0] == "TIME"):
        caller.Time = regResult[0][1]

    if(regResult[0][0] == "NMBR"):
        caller.Number = regResult[0][1]

    if(regResult[0][0] == "NAME"):
        caller.Name = regResult[0][1]
        pushNotification("Caller ID", caller.getId())

def buildSerial(deviceName):
    ser = serial.Serial(deviceName)
    ser.write(str.encode("AT\r"))
    ser.write(str.encode("AT+VCID=1\r"))

    return ser
