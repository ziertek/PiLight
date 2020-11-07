#!/usr/bin/sudo /bin/bash
systemctl stop PiLight.service
systemctl disable PiLight.service
rm /etc/systemd/system/PiLight.service
rm -R /opt/PiLight
