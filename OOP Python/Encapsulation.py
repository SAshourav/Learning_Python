class Payment:
    def __init__(self, price):
        self.__final_price = price + price*0.05

    def get_final_price(self):
        return self.__final_price

    def set_final_price(self, discount):
        self.__final_price = self.__final_price - self.__calculate_discount(discount)

    def __calculate_discount(self,discount): #we can not call it in object as this is private
        return self.__final_price*(discount/100)

book = Payment(10)
print(book.get_final_price())
book.__final_price = 0  #we can do this because it is a public variable
book.set_final_price(20)
print(book.get_final_price())

#for private variable we need to use get and set method