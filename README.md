
# AudioProbe

This probe was designed for my master's thesis.

## Deployment

Deploy the device as follows:

### Setting up WiFi and SSH
If accessing via SSH, make sure to set WiFi and username/password before using Raspberry Pi Imager.

### Cloning the Repository
1. Generate a new SSH key and add it to the SSH agent:
   - [Generating a new SSH key and adding it to the SSH agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
   - [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
   
2. Clone the repository:
   \`\`\`bash
   git clone git@github.com:jimcinbrisbane/audioprobe.git
   cd audioprobe
   \`\`\`

### Creating and Activating Virtual Environment
1. Create a virtual environment:
   \`\`\`bash
   python3 -m venv audioprobe
   \`\`\`

2. Activate the virtual environment:
   \`\`\`bash
   source ./env/bin/activate
   \`\`\`

### Testing and Setup
1. Test your speakers:
   \`\`\`bash
   python play.py
   \`\`\`

2. Download the mic port:
   \`\`\`bash
   sudo apt-get install libportaudio2
   \`\`\`

3. Set volume:
   \`\`\`bash
   amixer sset Master 80%
   \`\`\`

4. Test your mic:
   \`\`\`bash
   python record.py
   \`\`\`

### Installing Dependencies
1. Install the sounddevice package:
   \`\`\`bash
   python -m pip install sounddevice
   \`\`\`

2. Ensure Google Cloud is set up on your Pi:
   - [Google Cloud setup](https://cloud.google.com/python/docs/setup#linux)

3. Install Google Cloud SDK:
   - [GCP SDK installation](https://cloud.google.com/sdk/docs/install-sdk#linux)
   - Make sure to download \`google-cloud-cli-linux-arm.tar.gz\` because Pi is ARM-based.

4. Install MongoDB:
   \`\`\`bash
   python -m pip install pymongo
   \`\`\`

5. Set up ADC:
   - [Setting up ADC](https://cloud.google.com/docs/authentication/external/set-up-adc)

6. Set volume to a good range:
   \`\`\`bash
   amixer set Master 78%
   \`\`\`

### Running the Application
1. Run the application:
   \`\`\`bash
   python trigger.py
   \`\`\`

2. To set up auto-start, follow these steps:
   \`\`\`bash
   sudo nano /usr/local/bin/autostart.sh
   \`\`\`

3. Add the following content to \`autostart.sh\`:
   \`\`\`bash
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

   # Set Google application credentials
   export GOOGLE_APPLICATION_CREDENTIALS="/home/probe0/audioprobe/crafty-shield-267206-fd4e23b40aa7.json" # Adjust the path as needed

   # Run the trigger script
   python trigger.py
   \`\`\`

4. Make the script executable:
   \`\`\`bash
   sudo chmod +x /usr/local/bin/autostart.sh
   \`\`\`

5. Create a systemd service:
   \`\`\`bash
   sudo nano /etc/systemd/system/autostart.service
   \`\`\`

6. Add the following content to \`autostart.service\`:
   \`\`\`ini
   [Unit]
   Description=Run autostart script on network connection
   After=network-online.target

   [Service]
   Type=oneshot
   ExecStart=/usr/local/bin/autostart.sh
   RemainAfterExit=true

   [Install]
   WantedBy=network-online.target
   \`\`\`

7. Enable and start the service:
   \`\`\`bash
   sudo systemctl enable autostart.service
   sudo systemctl start autostart.service
   \`\`\`

8. Reboot to ensure everything starts correctly:
   \`\`\`bash
   sudo reboot
   \`\`\`

### Notes
- Make sure to adjust paths and filenames according to your specific setup.
- Ensure all required dependencies and permissions are correctly set up.

GG (Good Game!)
