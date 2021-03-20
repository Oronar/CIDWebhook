import serial
import time
import configparser
import os

from helpers import parseData, buildSerial

def main():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
    print("Starting serial connection")
    ser = buildSerial(config["APP"]["DEVICE"])

    while True:
        if(ser.inWaiting() > 0):
            data = ser.readline().decode("ascii").rstrip()     
            print(data)
            parseData(data)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
