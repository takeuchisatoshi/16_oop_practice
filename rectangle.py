class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    r1 = Rectangle(4, 3)
    # 3分課題
    area1 = r1.area() #面積を計算する
    print(area1) # 12が出力される

    r2 = Rectangle(10, 5)
    area2 = r2.area()
    print(area2)

