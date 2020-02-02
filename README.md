# touch_dnb
raspberry Pi and mpr121-based sampler

* initialise the card following these instructions: https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/3
* enable ssh by placing blank `ssh` file on boot partition
* put the card into the raspberry
* connect the ethernet cable
* connect the power cable
* on the mac: enable wifi internet sharing via ethernet
* wait for pi to boot - around 1 min
* log into pi by `ssh pi@raspberrypi.local`
* `sudo apt update`
* `sudo apt install python3-pip`
* `sudo apt-get install -y python-smbus`
* `sudo apt-get install -y i2c-tools`
* configure i2c: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
