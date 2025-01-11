class Pi:
    def __init__(self):
        print("Calculating area and circumference")

    def get_string(self):
        try:
            self.r = int(input("Enter radius: "))
        except ValueError:
            print("Enter a valid number!")
            self.r = " "

    def calculate_area(self):
        return 3.14 * self.r ** 2

    def calculate_circumference(self):
        return 2 * 3.14 * self.r

circle = Pi()
circle.get_string()

print("The area of the circle is: " + str(circle.calculate_area()))
print("The circumference of the circle is: " + str(circle.calculate_circumference()))