from cafe.Inventory.inventory import Inventory
from cafe.Coffee.coffee import Coffee
from cafe.Beverage.beverage import Beverage


class Application:
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        while True:
            print("1. 제품 판매")
            print("2. 제품 메뉴 추가")
            print("3. 프로그램 종료")
            action = input("원하는 작업 번호 입력:")

            if action == "1":
                self.handle_sale()
            elif action == "2":
                self.handle_add_menu()
            elif action == "3":
                print("프로그램 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해 주세요.")

    def handle_sale(self):
        inventory_items = self.inventory.get_inventory()
        # 인벤토리에 비어있을 경우
        if not inventory_items:
            print("판매할 커피가 없습니다. 먼저 커피를 추가하세요.")
            return
            # 인벤토리에 있을 경우
        print("판매할 커피를 선택하세요")
        for index, (name, product) in enumerate(inventory_items.items()):
            print(f"{index}. {product.get_name()} {product.get_price()}원")

        choice = int(input("번호를 입력하세요:"))
        coffeeList = list(inventory_items.keys())
        selected_coffee = inventory_items[coffeeList[choice]]
        print(f"{selected_coffee.get_name()}가 판매되었습니다. 가격은 f{selected_coffee.get_price()}입니다.")

    def handle_add_menu(self):
        product_type = input("제품 유형을 선택(커피, 음료):")
        name = input("제품 이름 입력:")
        price = int(input("제품 가격 입력:"))
        if product_type == "커피":
            caffeine = int(input("카페인 함량을 입력하세요:"))
            self.inventory.add_product(Coffee(name, price, caffeine))
        elif product_type == "음료":
            self.inventory.add_product(Beverage(name, price))
        else:
            print("잘못된 제품 유형입니다. 다시 시도해 주세요.")
