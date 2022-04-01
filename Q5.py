import math


class Shape:
    ID = 1

    def __init__(self):
        self.ID = Shape.ID
        Shape.ID += 1

    def print(self):
        if self.perimeter() is None:
            perimeter = 'undefined'
        else:
            perimeter = str(self.perimeter())

        if self.area() is None:
            area = 'undefined'
        else:
            area = str(self.area())

        string = str(self.ID) + ': ' + self.__class__.__name__ + ', perimeter: ' + perimeter + ', area: ' + area
        print(string)

    def perimeter(self):
        return None

    def area(self):
        return None


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return round(math.pi * 2 * self.radius, 5)

    def area(self):
        return round(math.pi * self.radius ** 2, 5)


class Ellipse(Shape):

    def __init__(self, a, b):
        super().__init__()
        if a < 0 or b < 0:
            self.a = None
            self.b = None
        elif a > b:
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a

    def area(self):
        if (self.a and self.b) is None:
            return None
        else:
            return round(math.pi * self.a * self.b, 5)

    def eccentricity(self):

        if (self.a and self.b) is None:
            return None
        else:
            return round((math.sqrt(self.a ** 2 - self.b ** 2)), 5)
        # eccentricity = round((math.sqrt(self.a ** 2 - self.b ** 2)), 2)
        #
        # if eccentricity > 0:
        #     return eccentricity
        # else:
        #     return None


class Rhombus(Shape):

    def __init__(self, p, q):
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self):
        return round(2 * math.sqrt(self.p**2 + self.q**2), 5)

    def area(self):
        return round((self.p * self.q) / 2, 2)

    def inradius(self):
        try:
            return round((self.p * self.q) / self.perimeter(), 5)
        except:
            return None
