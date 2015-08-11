'''
Copyright 2015 Stefan Andrei Chelariu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from libhmc5883l import hmc5883l
from time import sleep
from sys import exit

print "This is an example code for HMC5883L sensor library"

my_sensor = hmc5883l.HMC5883L(1) 

if my_sensor.set_parameter('meas_mode', 'continuous'):
	print "Set measurement mode to continuous"
else:
	exit("Could not set parameter, check I2C periph number")

print "Receiving Data" 

while True:
	print my_sensor.get_field_xyz()
	sleep(1)
	
