# Air Particle Monitoring Starter Solution

### Download
- Clone this repo `git clone https://github.com/DigitalShoestringSolutions/AirParticleMonitoring`
- Open the downloaded folder `cd AirParticleMonitoring`

### Configure
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
