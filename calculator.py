
class Calculator:
    def setUp(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return f"{self.number1} + {self.number2} = {self.number1 + self.number2}"

    def subtract(self):
        return f"{self.number1} - {self.number2} = {self.number1 - self.number2}"

    def division(self):
        return f"{self.number1} // {self.number2} = {self.number1 // self.number2}"

    def float_division(self):
        return f"{self.number1} / {self.number2} = {self.number1 / self.number2}"

    def multiple(self):
        return f"{self.number1} * {self.number2} = {self.number1 *  self.number2}"

result = Calculator()

result.setUp(2, 3)


print(result.add())
print(result.subtract())
print(result.division())
print(result.float_division())
print(result.multiple())
