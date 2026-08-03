class Engine:
    def start(self):
        print("Start by engine.")

class GasEngine:
    def start(self):
        print("Start by gasengine.")

class ElectricEngine:
    def start(self):
        print("Start by electricengine.")

class CarInternal:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

class CarExternal:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

car = CarInternal()
gas_car = CarExternal(GasEngine())
electric_car = CarExternal(ElectricEngine())

car.start()
gas_car.start()
electric_car.start()
