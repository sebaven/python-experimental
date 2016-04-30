class BirdTower:
    
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def print_info(self):
        print("tower name: " + self.name)
        print("latitude " + str(self.latitude))
        print("longitude: " + str(self.longitude))