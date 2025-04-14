class Smartphone: # Base class for smartphones
    def __init__(self, brand, model, storage, battery_life): # Constructor with private attributes
        self._brand = brand  # private attribute
        self._model = model  # private attribute
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number): # Method to make a call
        print(f"Calling {number}...")

    def send_message(self, number, message): # Method to send a message
        print(f"Sending message to {number}: {message}")

    def charge_battery(self, hours): # Method to charge the battery
        self.battery_life += hours
        print(f"Battery charged for {hours} hours. Current battery life: {self.battery_life} hours.")

    def get_brand(self): # Getter for brand
        return self._brand

    def get_model(self): # Getter for model
        return self._model

    def __str__(self):
        return f"{self._brand} {self._model} with {self.storage}GB storage and {self.battery_life} hours of battery life."


class PremiumSmartphone(Smartphone): # Inherits from Smartphone
    def __init__(self, brand, model, storage, battery_life, additional_feature): # Constructor with additional feature
        super().__init__(brand, model, storage, battery_life) # Call the parent constructor
        self.additional_feature = additional_feature # New attribute for premium feature

    def charge_battery(self, hours): # Override the charge_battery method
        self.battery_life += hours * 2  # Premium phones charge faster
        print(f"Premium battery charged for {hours} hours. Current battery life: {self.battery_life} hours.")

    def __str__(self):
        return super().__str__() + f" with additional feature: {self.additional_feature}"


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):# This method should be overridden in subclasses
        pass # This is an abstract method

class Car(Vehicle):# This class inherits from Vehicle
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):# This class inherits from Vehicle
    def move(self):
        print("Flying ✈️")# This class overrides the move method

# Testing the classes
if __name__ == "__main__":
    # Test smartphone classes
    phone1 = Smartphone("Apple", "iPhone 13", 128, 20)
    print(phone1)
    phone1.make_call("123-456-7890")
    phone1.charge_battery(2)

    phone2 = PremiumSmartphone("Samsung", "Galaxy S21", 256, 25, "Water Resistance")
    print(phone2)
    phone2.make_call("098-765-4321")
    phone2.charge_battery(2)

    # Test vehicle polymorphism
    print("\nVehicle Demonstration:")
    vehicles = [Car(), Plane()]
    for vehicle in vehicles:
        vehicle.move()
