class VoltageForceOperation:
    def __init__(self, unit, value: float, signal: str,
                 reference='GND', comment=None):
        self.unit = unit
        self.value = value

class CurrentForceOperation:
    def __init__(self):
        pass

class ResistanceForceOperation:
     pass 
