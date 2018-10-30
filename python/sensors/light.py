class Light:
	def __init__(self, id, serialNumber, name, sensorType, value, min, max):
		self.id = id
		self.serialNumber = serialNumber
		self.name = name
		self.type = sensorType
		self.value = value
		self.min = min
		self.max = max