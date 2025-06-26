
'''
{"mc_1p0": sample.mass_concentration_1p0.physical,
"mc_2p5": sample.mass_concentration_2p5.physical,
"mc_4p0": sample.mass_concentration_4p0.physical,
"mc_10p0": sample.mass_concentration_10p0.physical,
"ambient_rh": sample.ambient_humidity.percent_rh,
"ambient_t": sample.ambient_temperature.degrees_celsius,
"voc_index": sample.voc_index.scaled,
"nox_index": sample.nox_index.scaled,
}
'''

import logging

logger = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)  # move to log config file using python functionality

class ADC:
    def __init__(self, config):
        logger.info('pmso700x sensor initialised')
        