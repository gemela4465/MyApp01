# 汽車類別
class Cars:
# 建構式
    def __init__(self, weight):
        self.test = weight  # test 透過 settet 回覆值

    @property
    def fuck(self):
        print('這裡是 property')
        return self.__test2

    @fuck.setter
    def test(self, value):
        print('我近來囉')
        if value <= 0:
            raise ValueError("Car weight cannot be 0 or less.")
        self.__test2 = value

mazda = Cars(-200)
# mazda = Cars(-200)
print(mazda.fuck)