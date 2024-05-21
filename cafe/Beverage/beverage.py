from ..Product.product import Product

class Beverage(Product):
    def display_info(self):
        print(f"{self.name} - {self.price}원, 카페인 없습니다.")

