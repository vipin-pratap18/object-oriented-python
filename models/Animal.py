class Animal:

    
    def __init__(self):
        print("Animal class no arg constructor initialised")
        self.__species__ = "Animals of Earth"

    def get_species(self):
        return self.__species__

    def set_species(self, newValue):
        self.__species__ = newValue