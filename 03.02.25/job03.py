class Operation:
    def __init__(self, num1=5, num2=10):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        resultat = self.num1 + self.num2
        print("Result of the addition :", resultat)


num1 = 5
num2 = 10

# Instantiating the class with the chosen values
operation_instance = Operation(num1, num2)

print(operation_instance)

print("num1:", operation_instance.num1)
print("num2:", operation_instance.num2)

# Calling the addition method
operation_instance.addition()