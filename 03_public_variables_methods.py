class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"The {self.brand} car is starting...")

# Create an instance of the Car class
my_car = Car("Toyota")

# Access the public variable
print("Car Brand:", my_car.brand)

# Call the public method
my_car.start()
