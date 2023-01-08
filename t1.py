#汽車類別
class cars:
    #建構式
    def __init__(self,color,seat):
        self.color = color #顏色屬性
        self.seat = seat   #座位屬性

    #方法
    def dirve(self):
        print(f"My car is {self.color} and {self.seat} seats.")


#用 類別 指定 屬性 後成為一個 物件
ad = cars("Red",4)

ad.seat = 5

ad.dirve()

print (isinstance(ad,cars))

