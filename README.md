# dailyprophet

sudo apt install python3-pip mplayer
sudo pip install RPi.GPIO
sudo groupadd gpio
sudo usermod -a -G gpio ubuntu
sudo grep gpio /etc/group
sudo chown root.gpio /dev/gpiomem /dev/mem
sudo chmod g+rw /dev/gpiomem /dev/mem