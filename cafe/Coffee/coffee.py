from ..Product.product import Product


class Coffee(Product):
    def __init__(self, name, price, caffeine_content):
        super().__init__(name, price)
        self.caffeine_content = caffeine_content

    def display_info(self):
        print(f"{self.name} - {self.price}원, 카페인 함량: {self.caffeine_content}mg")
