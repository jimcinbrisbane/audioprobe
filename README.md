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
9. download mic port using "sudo apt-get install libportaudio2"
10. set volume  "amixer sset Master 80%"
11. test your mic using python record.py
12. install package using python -m pip install sounddevice
13. 
11. 
