class Combine:
    priceStaticField = 25000000
    numberOfSeatsStaticField = 5
    __colorPrivateField = "Green"

    def __init__(self, hopperVolumeInKg=0, fuelConsumptionPer1Ha=0, enginePowerInHorsePower=0,
    model="Choose,please",speedInKmPerHour=0,producingCountry="Ukraine"):
        self.hopperVolumeInKg = hopperVolumeInKg
        self.fuelConsumptionPer1Ha = fuelConsumptionPer1Ha
        self.enginePowerInHorsePower = enginePowerInHorsePower
        self.model = model
        self.speedInKmPerHour = speedInKmPerHour
        self.producingCountry = producingCountry

    def __del__(self):
        pass

    def __str__(self):
        return "Hopper Volume In Kg is  {} \t Fuel Consumption Per 1 Ha is {} \t Engine Power In HorsePower is {}" \
               "\t Combine Model is {} \t Speed In Km Per Hour is {}\t Producing Country is {}"\
            .format(self.hopperVolumeInKg, self.fuelConsumptionPer1Ha, self.enginePowerInHorsePower, self.model,
                    self.speedInKmPerHour, self.producingCountry)
    @staticmethod
    def priceStaticMethod():
       return Combine.priceStaticField

    @staticmethod
    def numberOfSeatsStaticMethod():
        return Combine.numberOfSeatsStaticField

    def colorGetter(self):
        return self.__colorPrivateField

    def colourSetter(self, colorPrivateField):
        self.__colorPrivateField = colorPrivateField




