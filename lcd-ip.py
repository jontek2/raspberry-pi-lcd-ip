#!/usr/bin/python

import Adafruit_CharLCD as LCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = LCD.Adafruit_CharLCDPlate()

cmd = "ip -4 addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd2 ="wget -qO- ifconfig.me/ip"

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        output = p.communicate()[0]
        if p.returncode != 0:
                return None
        return output

lcd.message("Obtaining IP\n")
lcd.message("...")
while 1:
        lcd.clear()
        ipaddr = run_cmd(cmd)
        ipaddr2 = run_cmd(cmd2)
        if ipaddr:
                lcd.message(ipaddr2)
                lcd.message(ipaddr)
                sleep(10)
                lcd.set_color(0, 0, 0)
                break
        sleep(5)