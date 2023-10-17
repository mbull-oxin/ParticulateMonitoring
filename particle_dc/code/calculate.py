# ----------------------------------------------------------------------
#
#    Air Particle Monitoring -- This digital solution measures,
#    reports and records PM, Ambient temperature and humidity in the environment. 
#    This version comes with one current transformer 
#     The solution provides a Grafana dashboard that 
#    displays PM,temperature and humidity, and an InfluxDB database 
#    to store timestamp, PM, temperature and humidity. 
#
#    Copyright (C) 2022  Shoestring and University of Cambridge
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see https://www.gnu.org/licenses/.
#
# ----------------------------------------------------------------------

import logging
import math

logger = logging.getLogger("main.measure.conversion")


class AirParticleMonitoringCalculation:
    one_over_sqrt_2 = 1 / math.sqrt(2)

    def __init__(self, config):
        return
        

    def calculate(self, ADCsamples):
        # Access each physical value (as floats) separately:
        mc_1p0 = ADCsamples.mass_concentration_1p0.physical
        mc_2p5 = ADCsamples.mass_concentration_2p5.physical
        mc_4p0 = ADCsamples.mass_concentration_4p0.physical
        mc_10p0 = ADCsamples.mass_concentration_10p0.physical
        ambient_rh = ADCsamples.ambient_humidity.percent_rh
        ambient_t = ADCsamples.ambient_temperature.degrees_celsius
        voc_index = ADCsamples.voc_index.scaled
        nox_index = ADCsamples.nox_index.scaled

        return {"mc_1p0": str(mc_1p0), "mc_2p5": str(mc_2p5), "mc_4p0": str(mc_4p0),"mc_10p0": str(mc_10p0), "ambient_rh": str(ambient_rh),
        "ambient_t": str(ambient_t), "voc_index": str(voc_index), "nox_index": str(nox_index)}
