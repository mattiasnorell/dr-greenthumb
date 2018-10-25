from sensors.sensorbase import SensorBase

class Temperature(SensorBase):
	def __init__(self, id, serialNumber, name, type, temperature, min, max):
		super().__init__(self, id, serialNumber, name, type, temperature, min, max)
		self.temperature = temperature