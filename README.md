# audioprobe
probe designed for my master's thesis

deploy the device into
1. if accessing via SSH make sure to set wifi and username pw before using Raspberry Pi Imager
2. clone using ssh
   see https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux
   and https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
   then use
3. git clone git@github.com:jimcinbrisbane/audioprobe.git
4. cd audioprobe
5. create virtual env using python3 -m venv audioprobe
6. use it  source ./env/bin/activate
8. test your speakers using python play.py
9. download the mic port using "sudo apt-get install libportaudio2"
10. set volume  "amixer sset Master 80%"
11. test your mic using python record.py
12. install the package using python -m pip install sounddevice
13. ensure google cloud is set up in your pi, see https://cloud.google.com/python/docs/setup#linux
14. you probably need gcp https://cloud.google.com/sdk/docs/install-sdk#linux
15. since we're installing it on pi make sure you're downloading google-cloud-cli-linux-arm.tar.gz because pi is arm-based
16. install MongoDB python -m pip install pymongo
17. set up adc https://cloud.google.com/docs/authentication/external/set-up-adc
18. set volume to a good range, like "amixer set Master 78%"
19. either run via python trigger.py or try setting up auto start


## set up auto start
1.  sudo nano /usr/local/bin/autostart.sh

#!/bin/bash
cd /home/probe0/audioprobe
# Configure ALSA defaults
echo -e "defaults.pcm.card 1\ndefaults.ctl.card 1" > /etc/asound.conf

# Ensure user permissions for audio
sudo usermod -aG audio $USER

# Start PulseAudio (if needed)
pulseaudio --start

# Activate the virtual environment
source /home/probe0/audioprobe/env/bin/activate

# Set the SDL audio driver to ALSA
export SDL_AUDIODRIVER=alsa
export GOOGLE_APPLICATION_CREDENTIALS="/home/probe0/audioprobe/crafty-shield-267206-fd4e23b40aa7.json" 
#depends on your device name, where you set up the git and where you hide the JSON file for your GCP project
python trigger.py

3. sudo chmod +x /usr/local/bin/autostart.sh

4. sudo nano /etc/systemd/system/autostart.service
[Unit]
Description=Run autostart script on network connection
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/autostart.sh
RemainAfterExit=true

[Install]
WantedBy=network-online.target

5. sudo systemctl enable autostart.service
6. sudo systemctl start autostart.service to see if it start
7. then sudo reboot
8. gg





