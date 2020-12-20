# PiLight
<sub>Version: 0.5</sub>

* [Introduction](#Introduction)
* [Hardware](#Hardware)
    * [Shopping List](#Shopping)
    * [Build Instructions](#Build)
* [Installation](#Installation)
* [Usage](#Usage)
* [Config Files](#Config)
* [ToDo](#ToDo)
* [License](#License)

# Introduction
Like many other people I ran into estruyf's Unicorn Busy Light project and was inspired to build one as well.  You can find the original repo here: https://github.com/estruyf/unicorn-busy-server and his blog post about it here: https://www.eliostruyf.com/diy-building-busy-light-show-microsoft-teams-presence/.  Personally, I hadn't done any real coding in 10+ years and very little with Python so I when I attempted to fork the project and build some customizations I was fairly overwhelmed.  As a result, I built out this new project instead of using a fork.  Code has been borrowed from estruyf as well as j-maynard who forked the project too (https://github.com/j-maynard/unicorn-busy-server).

# Hardware
Of course you can build this with in many different variations but here I list everything I used and how I assembled it.  I bought most of my stuff from Pimorani directly as I was getting the Unicorn pHat there anyways, but many items can also be found elsewhere like amazon.

## <a id="Shopping"></a>Shopping List:
| Part | Quantity | Cost | URL | Notes |
|------|:----------:|:------:|-----|-------|
| PiZero W | 1 | $15.00 | [Pimoroni](https://shop.pimoroni.com/products/raspberry-pi-zero-w) [Amazon](https://www.amazon.ca/Raspberry-Pi-Zero-W/dp/B06XFZC3BX/ref=sr_1_5) |  |
| Unicorn pHat | 1 | $18.00 | [Pimoroni](https://shop.pimoroni.com/products/unicorn-phat) | LED Hat |
| pHat Diffuser | 1 | $5.00 | [Pimoroni](https://shop.pimoroni.com/products/phat-diffuser) | The LEDs are quite bright, the deffuser makes it much nicer |
| Pibow Zero W | 1 | $8.00 | [Pimoroni](https://shop.pimoroni.com/products/pibow-zero-w) | Case for the Pi.  Many options are out there. |
| Pogo Pins | 3 | $10.00 | [Pimoroni](https://shop.pimoroni.com/products/pogo-a-go-go-solderless-gpio-pogo-pins) | Only need 3, most places offer packs with many more. |
| M2.5 Nylon Nuts & Bolts | 8 | $15.00 | [Pimoroni](https://shop.pimoroni.com/products/pibow-extender-bolt-pack) | I had some M3 ones from a previous project from [Amazon](https://www.amazon.ca/Metric-Plastic-Machine-Assortment-M3X5mm/dp/B073F6Q66G/ref=sxts_sxwds-bia-wc-nc-drs1_0) that I used.  They were tight but worked. |

Note prices are approximate and in Canadian Dollars with Canadian store links.  Pimoroni does show their price in CAD if you set the website to do so, but it does still ship from the UK.

You will also need:<br>
    * Micro-USB powersupply<br>
    * Micro-USB OTG<br>
    * Mini HDMI cable/adapter<br>
    * 16GB or larger MicroSD card<br>
    * Monitor with HDMI<br>
    * Keyboard/mouse<br>
If you've used a Pi Zero before you likely have the Keyboard/Mouse, Monitor, HDMI Adapter, OTG Adapter and Powersupply around.

## <a id="Build"></a>Build Instructions:
1) Install RaspberryPi OS Lite on SD Card
    I have the Raspberry Pi Imager installed on my laptop.  Makes it really simple to image a MicroSD with a supported OS.  You can find instructions [here](https://www.raspberrypi.org/documentation/installation/installing-images/) from the Raspberry Pi Website.
2) Assemble Pi
    Put Micro SD in the Pi and assemble the case.  If you used the Pibow you can follow their instructions [here](https://learn.pimoroni.com/tutorial/sandyj/pibow-zero-assembly)
3) Power up Pi and setup OS
    Plugin the monitor, OTG, Keyboard/Mouse, and finally power and walk through the OS setup.  SparkFun has a pretty good page on how to setup the OS [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless/all).
4) Connect Hat
    Place the pogo pins on pins 2, 6, and 12 [pinout](https://pinout.xyz/pinout/unicorn_phat).
        NOTE: I found that the hat wouldn't work when I put the pogo pins right side up.  I instead put the pogo pins in the had's GPIO and put the Pi and case down onto the hat.
    Place hat on top, ensure the pins line up with the hat.
    Use bolts to to bolt LEDs and Diffuser down.
5) Boot up and setup the software

# Installation
The installer has been setup to download the files should they be needed so you should be able to simply install curl (if it isn't already) and run the installer from the like so:
```bash
sudo apt install git
curl -sSL https://raw.githubusercontent.com/ziertek/PiLight/master/installers/install.sh | sudo bash -
```
The Installer will install PiLight into the /opt/ directory by default but you can change the location using the -i argument.  The installer also setups up a service for PiLight.  If you don't want the service simply clone/download the repo and run:
```bash
sudo pip install -r .\requirements.txt
sudo python server.py
```

Arguements:
```bash
  -i  --install-dir        Specify where you want to install to
                           Default is: /opt/PiLight
  -V  --verbose            Shows command output for debugging
  -v  --version            Shows version details
  -h  --help               Shows this usage message
```

# Usage
When you install PiLight with the installer above it will automatically setup a service called PiLight.service.  This should start once the installer is done and any time the Pi is powered on.  Once the service has started the LEDs will set to White.  Once you see that you can browse to the webpage at http://*Pi-IP-Address*:5000/ and set the colours.

The PiLight is meant to be controlled by an agent or external app to change the colours automateically, removing the need to click a button on the web UI.  The API endpoints are as follows:

| Method(s) | Endpoint | Description |
|:------:|-------|-------|
| [**GET**](#colour) | /api/colour/*Colour* | Change the hat to the designated Colour | 
| [**GET**](#rainbow) | /api/colour/Rainbow | Set the hat to display a scrolling rainbox |
| [**GET**](#Blank) | /api/colour/Blank | Turns off the LEDs on the hat |
| [**GET**](#Updatepi) | /api/system/UpdatePi | Updates the Pi OS using apt-get and completes a reboot | 
| [**GET**](#shutdown) | /api/system/Shutdown | Shuts down the Pi so it can be safely unplugged |

## <a id="colour"></a> Display Colour
Will display the colour that was specified.  The options are:<br>
 * Green<br>
 * Red<br>
 * Yellow<br>
 * Blue<br>
 * Pink<br>
 * Teal<br>

## <a id="rainbow"></a> Display rainbow
Will display a scrolling rainbow on the hat.

## <a id="blank"></a> Blank
Turns off the LEDs on the hat.

## <a id="updatepi"></a> Update Pi
Runs the update script that will get all updates for the OS (assumed Raspberry OS currently), install them, and then reboot.

## <a id="shutdown"></a> Shutdown Pi
Runs a "Shutdown now" command on the OS to shutdown the Pi allowing it to be safely unplugged.  I recommend giving the Pi 30 seconds or so before unplugging it.


# Config Files
PiLight uses YAML config files to get and set some standard values.  Inside the lib folder you will find the config_default.yaml which is used for default values on the app.  You can also create a config.yaml in the /etc/PiLight/ directory of your Linux OS which can store your personal values.  If a value is not in your personal config.yaml file the value will instead be pulled from the config_default.yaml file.  This allows you to only set values you want to change and easily remove values to go back to working ones.

I use the confuse library to import the config.  If you are curious about it, you can check it out here: https://github.com/beetbox/confuse

# ToDo
 - [ ] Add support for self updating
 - [ ] Add some animations and icons
 - [ ] Setup Favicon (have display the current status)
 - [ ] Setup Status section on front end
 - [X] Put webpage name in config.yaml
 - [X] Put colour lables in config.yaml
 - [ ] Add Get-Status in API
 - [ ] Add support for Blinkt
 - [ ] Add support for Unicorn hat (full sized)
 - [ ] Add support for Unicorn mini
 - [ ] Look at Home Assistant integration (https://www.home-assistant.io)

 # License

 **MIT License**

 Copyright (c) 2020 [*Braden Magnan*](https://github.com/ziertek)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
