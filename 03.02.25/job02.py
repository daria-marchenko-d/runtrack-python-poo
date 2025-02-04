class Operation:
    def __init__(self, num1=5, num2=10):
        self.num1 = num1
        self.num2 = num2

num1 = 5
num2 = 10

# Instantiating the class with the chosen values
operation_instance = Operation(num1, num2)

print(operation_instance)

print("number 1:", operation_instance.num1)
print("number 2:", operation_instance.num2)