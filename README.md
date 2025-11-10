# Air Particle Monitoring Starter Solution

## Install the Shoestring App
In the terminal, run:
- `sudo apt instll pipx -y`
- `sudo pipx run shoestring-setup`
- `sudo reboot` if prompted to restart

## Use the Shoestring App to download and configure this Solution
- In the terminal run `shoestring app`, or double click the desktop icon called `Shoestring`.  
- Use the `Download` button to select the name of this solution. Select the latest release tag.  
- Follow the prompts to configure

## Build & Start
Continue accepting the prompts to build and start now

### Usage
- View the dashboard: navigate to `localhost:3000` in a web browser
![image](https://github.com/user-attachments/assets/3dadfb51-528b-4f49-a816-dc73d2670d06)

### Documentation
- documentation for gravity HCHO Sensor
https://wiki.dfrobot.com/Gravity__HCHO_Sensor_SKU__SEN0231#More

### Changes
- this repo has changes for implementation of addon sensors alongside the particulate monitors, these can only add a single extra reading and utilize the new add_type, add_unit and add_reading keys in the MQTT packet.
