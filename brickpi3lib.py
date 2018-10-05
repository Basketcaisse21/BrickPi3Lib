import brickpi3
import time

class Sensor:
	bp = None
	type = None
	slot = None
	
	def __init__(self, slot, type):
		self.bp = brickpi3.BrickPi3()
		slot = self.__setSlot(slot)
		if slot:
			self.slot = slot
			if type == "ultrasonic" or type == "ultra" or type=="us":
				self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_ULTRASONIC_CM)
			elif type == "infrared" or type == "ir":
				self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_INFRARED_REMOTE)
			elif type == "infraredproximity" or type == "irproxmiity" or type == "irp":
				self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)
			elif type == "gyro":
				self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
			elif type == "color" or type == "raw":
				self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_COLOR_COLOR)
			else:
				return False
			
		else:
			return False
			
	def __setSlot(self, slot):
		slot = slot.lower()
		if slot == "s1":
			return self.bp.PORT_1
		if slot == "s2":
			return self.bp.PORT_2
		if slot == "s3":
			return self.bp.PORT_3
		if slot == "s4":
			return self.bp.PORT_4
		return None
		
	def getVal(self):
		return self.bp.get_sensor(self.slot)
		
	def reset(self):
		return self.bp.reset_all()

class Motor:
	bp = None
	type = None
	slot = None
	
	def __init__(self, slot):
		self.bp = brickpi3.BrickPi3()
		slot = self.__setSlot(slot)
		if slot:
			self.slot = slot
			self.setSpeed(0)
	
	def __setSlot(self, slot):
		slot = slot.lower()
		if slot == "ma":
			return self.bp.PORT_A
		if slot == "mb":
			return self.bp.PORT_B
		if slot == "mc":
			return self.bp.PORT_C
		if slot == "md":
			return self.bp.PORT_D
		return None
			
	def setSpeed(self, speed):
		self.bp.set_motor_power(self.slot, speed)



