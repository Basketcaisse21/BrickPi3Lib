import brickpi3

class Sensor:
	bp = None
	type = None
	slot = None
	slots = {
		"s1": self.bp.PORT_1,
		"s2": self.bp.PORT_2,
		"s3": self.bp.PORT_3,
		"s4": self.bp.PORT_4
	}
	
	def __init__(self, slot, type):
		self.bp = brickpi3.BrickPi3()
		slot = self.__setSlot(slot)
		if slot:
			self.__setType(type)
			
	def __setSlot(self, slot):
		slot = slot.lower()
		if slot in self.slots:
			selt.slot = slot
			return True
		return False
	
	def __setType(self, type):
		if type in ["ultrasonic", "ultra", "us"]:
			self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_ULTRASONIC_CM)
			return True
		elif type in ["infrared", "ir"]:
			self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_INFRARED_REMOTE)
			return True
		elif type in ["infraredproximity", "irproxmiity", "irp"]:
			self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)
			return True
		elif type in ["gyro"]:
			self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
			return True
		elif type in ["color", "raw"]:
			self.bp.set_sensor_type(slot, self.bp.SENSOR_TYPE.EV3_COLOR_COLOR)
			return True
		return False
		
	def getReading(self):
		return self.bp.get_sensor(self.slot)
		
	def reset(self):
		return self.bp.reset_all()

class Motor:
	bp = None
	type = None
	slot = None
	slots = {
		'ma': self.bp.PORT_A,
		'mb': self.bp.PORT_B,
		'mc': self.bp.PORT_C,
		'md': self.bp.PORT_D
	}
	
	def __init__(self, slot):
		self.bp = brickpi3.BrickPi3()
		slot = self.__setSlot(slot)
	
	def __setSlot(self, slot):
		slot = slot.lower()
		if slot in self.slots:
			self.slot = slots[slot]
			self.setSpeed(0)
			return True
		return False
			
	def setSpeed(self, speed):
		try:
			self.bp.set_motor_power(self.slot, speed)
			return True
		except:
			return False
		
	def reset(self):
		return self.bp.reset_all()
			
