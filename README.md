
# Hello, I'm Dr. Greenthumb
Automated greenhouse

## Install
sudo apt install python3-pip git

pip3 install RPi.GPIO flask flask_cors schedule yyaml picamera

## GUI
I use BusyBox httpd to serve the gui since it's a part of the Rasberry OS image and require zero configuration. 

**Start**
busybox httpd -p IP_ADDRESS:8080 -h /path/to/dr-greenthumb

**Quit**
pkill busybox
