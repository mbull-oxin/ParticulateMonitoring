import _thread,struct,serial

class Sensor:
    def __init__(self,config):
        self.config=config
        self._dev=self.connect(config)
        self.mutex=_thread.allocate_lock()
        self.tid=_thread.start_new_thread(self.main,())
        # adjust this to default reading coming from sensor...
        self.last_reading=0
    def connect(self,config):
        # TODO: connect i2c / spi / serial port to be passed to _sample
        pass
    def main(self):
        while 1:
            reading=self._sample(self._dev,self.config['adc']['sample_rate'])
            if reading:
                #we didn't timeout and have a reading...
                with self.mutex:
                    self.last_reading=reading
    def _sample(self,dev,tmo):
        st_byte=dev.read(1)
        while st_byte!=0xff:
            st_byte=dev.read(1)
        _bytes=dev.read(8)
        chksum=0
        for ind in range(7):
            chksum=(chksum+_bytes[ind]) & 0xff
        if _bytes[8]!=(~chksum) + 1:
            # failed chksum....
            print('ERROR: failed chksum in sen0231')
            return None
        return struct.unpack('>xxxHxx',_bytes[:-1])[0]
    def sample(self):
        with self.mutex:
            return {'add_type':'HCHO','add_units':'ppm','add_reading':self.last_reading/1000}