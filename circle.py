class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * 3.14

    def circumference(self):
        return 2 * self.radius * 3.14


if __name__ == '__main__':
    circle = Circle(radius=3)
    print(circle.area())
    print(circle.circumference())

    circle2 = Circle(20)
    print(circle2.area())
    print(circle2.circumference())

    input_number = int(input("数字を入力"))
    circle3 = Circle(input_number)
    print(circle3.area())
    print(circle3.circumference())

    # print(circle.radius) サンプル
