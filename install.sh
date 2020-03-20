#!/bin/sh
echo "I never said this would work

If you arent on a raspi 0, consider reading this file"

sudo apt update & # Multithreading? just a mess? you think I know?
aptpid=$!
# This is pre-built, so I just hope that it installs smoothly, you can install from source if that floats your boat
cd bluez-5.41/
sudo make install

wait $aptpid
sudo apt-get install python-bluez python-requests

echo "I hope to god that worked"


#proper install here, but aint nobody got time 4 that, the default should work on a raspi 0 w
#sudo apt-get install -y libudev-dev dbus libdbus*dev libical-dev libreadline-dev libglib2.0-dev
