import _thread,struct,serial,logging

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
        prt=serial.Serial('/dev/ttyS0',baudrate=9600)
        return prt
    def main(self):
        while 1:
            #print('measurement cycle')
            reading=self._sample(self._dev,self.config['sampling']['sample_interval'])
            #print(reading)
            if reading:
                #we didn't timeout and have a reading...
                with self.mutex:
                    self.last_reading=reading
    def _sample(self,dev,tmo):
        st_byte=dev.read(1)
        while st_byte!=b'\xff':
            st_byte=dev.read(1)
        _bytes=dev.read(8)
        chksum=0
        for ind in range(7):
            chksum=(chksum+_bytes[ind]) & 0xff
        if _bytes[7]!=~chksum+257:
            # failed chksum....
            logging.error('failed chksum in sen0231')
            return None
        #print('packet %s - result %s' % (repr(_bytes),struct.unpack('>xxHxx',_bytes[1:-1])))
        return struct.unpack('>xxHxx',_bytes[1:-1])[0]
    def sample(self):
        with self.mutex:
            return {'add_type':'HCHO','add_units':'ppb','add_reading':self.last_reading}

if __name__=='__main__':
    import time
    sns=Sensor({'sampling':{'sample_interval':1}})
    while 1:
        time.sleep(2)
        print(sns.sample())