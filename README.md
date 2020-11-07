# PiLight
WARNING: This readme is still a work in progress.

* [Introduction](#Introduction)
* [Hardware](#Hardware)
    * [Shopping List](#Shopping)
    * [Build Instructions](#Build)

# Introduction
Like many other people I ran into estruyf's Unicorn Busy Light project and was inspired to build one as well.  You can find the original repo here: https://github.com/estruyf/unicorn-busy-server and his blog post about it here: https://www.eliostruyf.com/diy-building-busy-light-show-microsoft-teams-presence/.  Personally, I hadn't done any real coding in 10+ years and very little with Python so I when I attempted to fork the project and build some customizations I was fairly overwhelmed.  As a result, I built out this new project instead of using a fork.  Code has been borrowed from estruyf as well as j-maynard who forked the project too (https://github.com/j-maynard/unicorn-busy-server).

# Hardware
Of course you can build this with in many different variations but here I list everything I used and how I assembled it.  I bought most of my stuff from Pimorani directly as I was getting the Unicorn pHat there anyways, but many items can also be found elsewhere like amazon.

## <a id="Shopping"></a>Shopping List:
| Part | Quantity | Cost | URL | Notes |
| PiZero W | 1 | $15.00 | [Pimoroni](https://shop.pimoroni.com/products/raspberry-pi-zero-w) [Amazon](https://www.amazon.ca/Raspberry-Pi-Zero-W/dp/B06XFZC3BX/ref=sr_1_5) |  |
| Unicorn pHat | 1 | $18.00 | [Pimoroni](https://shop.pimoroni.com/products/unicorn-phat) | LED Hat |
| Pibow Zero W | 1 | $8.00 | [Pimoroni](https://shop.pimoroni.com/products/pibow-zero-w) | Case for the Pi.  Many options are out there, I ran with this since I was buying from Pimoroni already. |
| Pogo Pins | 3 | $10.00 | [Pimoroni](https://shop.pimoroni.com/products/pogo-a-go-go-solderless-gpio-pogo-pins) | Only need 3, most places offer packs with many more. |
| M2.5 Nylon Nuts & Bolts | $15.00 | [Pimoroni](https://shop.pimoroni.com/products/pibow-extender-bolt-pack) | I had some M3 ones from a previous project from [Amazon](https://www.amazon.ca/Metric-Plastic-Machine-Assortment-M3X5mm/dp/B073F6Q66G/ref=sxts_sxwds-bia-wc-nc-drs1_0) that I used.  They were tight but worked. |
Note prices are approximate and in Canadian Dollars with Canadian store links.  Pimoroni does show their price in CAD if you set the website to do so, but it does still ship from the UK.

You will also need:
    * Micro-USB powersupply
    * Micro-USB OTG
    * Mini HDMI cable/adapter
    * Monitor with HDMI
    * Keyboard/mouse
If you've used a Pi Zero before you likely have the Keyboard/Mouse, Monitor, HDMI Adapter, OTG Adapter and Powersupply around.

## <a id="Build"></a>Build Instructions:
