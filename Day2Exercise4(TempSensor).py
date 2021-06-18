#!/usr/bin/python
import RPi.GPIO as GPIO
import time, re, os, glob

pins = [40]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.IN)

#access file
os.system("modpro w1-gpio")
os.system("modpro w1-therm")
basedir = "/sys/bus/w1/devices/"
devicedir = glob.glob(basedir + "28*")[0]
devicefile = devicedir + "/w1_slave"


def gettemp():
    print("Getting temperature")
    fh = open(devicefile, "r")
    lines = fh.readlines()
    fh.close()
    
    match = re.search("t=(\d+)", lines[1])
    print(float(match.group(1)) / 1000)
    
if __name__ == "__main__":
    try:
        while True:
            gettemp()
            time.sleep(1)
    except (KeyboardInterrupt):
        pass;
    