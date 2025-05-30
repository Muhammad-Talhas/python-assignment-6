class Logger:
    def __init__(self):                         #constructor
        print("Logger objecte is created!")
    
    def __del__(self):                          #descrtutor
        print("Logger object is deleted!")

print("Entering main function...")
# Create an object of the class
log1 = Logger()                         
print("Doing some work...")
del log1
print("Exiting main function...")
        