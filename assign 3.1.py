class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setWidth(self, w):
        self.width = w

    def setHeight(self, h):
        self.height = h



def area_difference(r1, r2):
    return r1.area() - r2.area()


if __name__ == "__main__":
    r = Rectangle(5, 4)
    print(f"Initial Area: {r.area()}, Initial Perimeter: {r.perimeter()}")


    r.setWidth(10)
    r.setHeight(15)
    print(f"Updated Width: {r.getWidth()}, Updated Height: {r.getHeight()}")
    print(f"Updated Area: {r.area()}, Updated Perimeter: {r.perimeter()}")

    print("-" * 40)

    r1 = Rectangle(10, 10)
    r2 = Rectangle(15, 20)

    diff = area_difference(r1, r2)
    print(f"The signed area difference between r1 and r2 is: {diff}")