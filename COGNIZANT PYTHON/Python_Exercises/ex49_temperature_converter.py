class Converter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

temp = float(input("Enter Celsius: "))

obj = Converter()

print("Fahrenheit:", round(obj.c_to_f(temp), 2))