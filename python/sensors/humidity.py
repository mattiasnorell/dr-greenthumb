from SensorBase import SensorBase

class Humidity(SensorBase):
	def __init__(self, id, serialNumber, name, type, value, min, max):
		super().__init__(self, id, serialNumber, name, type, value, min, max)
