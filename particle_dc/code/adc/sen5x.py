import time
from sensirion_i2c_driver import I2cConnection, LinuxI2cTransceiver
from sensirion_i2c_sen5x import Sen5xI2cDevice
import logging

logger = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)  # move to log config file using python functionality

class ADC:
    def __init__(self, config):
        logger.info(f"init sen5x")
        #with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
        i2c_transceiver = LinuxI2cTransceiver('/dev/i2c-1')
        self.device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))
        # Print some device information
        logger.info(f"Sensor Version:{self.device.get_version()}")
        logger.info(f"Product Name:{self.device.get_product_name()}")
        logger.info(f"Serial Number:{self.device.get_serial_number()}")
            
        # Perform a device reset (reboot firmware)
        self.device.device_reset()
        logger.debug(f"start measurement")
        self.device.start_measurement()
       
            

       
        
    def sample(self):
      
        
            
        logger.debug(f"Waiting for new data...")
        # Wait until next result is available  
        while self.device.read_data_ready() is False:
            time.sleep(0.5)

        # Read measured values -> clears the "data ready" flag
        values = self.device.read_measured_values()
                
        logger.info(f"RAW Values:{values}")

        # Access a specific value separately (see Sen5xMeasuredValues)
        #mass_concentration = values.mass_concentration_2p5.physical
        #ambient_temperature = values.ambient_temperature.degrees_celsius

        # Read device status
        status = self.device.read_device_status()
        logger.info(f"Device Status:{status}")


        # Stop measurement
        #self.device.stop_measurement()
        #logger.info(f"Measurement stopped")
        return values



   
