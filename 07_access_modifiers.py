class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected 
        self.__ssn = ssn          # Private 

# Create an object of the class
emp1 = Employee("Ali", 50000, "123-45-6789")

# Accessing variables
print("Public: Name =", emp1.name)        # ✅ Accessible

print("Protected: Salary =", emp1._salary)  # ⚠️ Accessible
# Attempting to access private variable
try:
    print("Private: SSN =", emp1.__ssn)   # ❌ Will raise AttributeError
except AttributeError as e:
    print("Private: Cannot access __ssn directly! Error:", e)

