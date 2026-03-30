# Air Particle Monitoring Starter Solution

### Download
- Clone this repo
```bash
  git clone https://github.com/mbull-oxin/ParticulateMonitoring.git
```
### Install Docker
- Install docker
```vbash
curl -sSL https://get.docker.com | sh
```
- Add user to the docker group
```bash
sudo usermod -a -G docker $USER
```
- Set docker to run on startup
```bash
sudo systemctl enable docker
```

### Setup I2c
- Launch raspi-config
```bash
sudo raspi-config
```
- Navigate to - Interface Options -> I2C -> <YES>
- then <FINISH> to exit
- select yes to reboot

### Setup Logging
- Download logging files
```bash
git clone https://github.com/DigitalShoestringSolutions/SetupLogging -b v1.1.2 ~/SetupLogging
```
- run script to setup logging 
```bash
~/SetupLogging/setup_logging.sh
```

### Configure
- Change to the downloaded folder from earlier `cd ParticulateMonitoring` 
- Set the machine name `nano particle_dc/config/config.toml`

### Build & Run
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`

### Usage
- View the dashboard: navigate to `localhost:3000` in a web browser
![image](https://github.com/user-attachments/assets/3dadfb51-528b-4f49-a816-dc73d2670d06)

### Documentation
- documentation for gravity HCHO Sensor
https://wiki.dfrobot.com/Gravity__HCHO_Sensor_SKU__SEN0231#More

### Changes
- this repo has changes for implementation of addon sensors alongside the particulate monitors, these can only add a single extra reading and utilize the new add_type, add_unit and add_reading keys in the MQTT packet.
