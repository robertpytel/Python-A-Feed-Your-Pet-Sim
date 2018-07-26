# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:39:27 2018
@author: robertp
Sources:

"""
from numpy as np
gyro_laccel = np.genfromtxt('Sensor_record_7_24_18_AndroSensor.csv', delimiter=',')
print(gyro_laccel)
