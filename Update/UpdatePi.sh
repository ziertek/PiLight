#!/bin/bash
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>UpdatePi.log 2>&1
# Everything below will go to the file 'UpdatePi.log':
date
apt-get update && apt-get full-upgrade -y
apt-get autoremove
apt-get autoclean
shutdown -r now