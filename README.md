# What

A simple python script that displays the ip of an Raspberry Pi on a Adafruit LCD. The script will light up the display for 10 sec and then turn the light off, but still display the IP:s.

![Image of output](http://www.jonathanhellman.se/wp-content/uploads/2017/08/lcd.png)

# Librarys

The script utilizes https://github.com/adafruit/Adafruit_Python_CharLCD

# Init boot

## Create A Unit File

````
sudo nano /lib/systemd/system/myscript.service
````


````
[Unit]
Description=My Script Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/pi/myscript.py

[Install]
WantedBy=multi-user.target
````


````
ExecStart=/usr/bin/python /home/pi/myscript.py > /home/pi/myscript.log 2>&1
````


````
sudo chmod 644 /lib/systemd/system/myscript.service
````

## Configure systemd

````
sudo systemctl daemon-reload
 sudo systemctl enable myscript.service
````


````
sudo reboot
````

## Check status of your service

````
sudo systemctl status myscript.service
````