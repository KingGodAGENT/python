from cafe.Inventory.inventory import Inventory
from cafe.Coffee.coffee import Coffee

class Application():
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        while True:
            print('1. 커피 판매')
            print('2. 커피 메뉴 추가')
            print('3. 프로그램 종료')
            action = input("원하는 작업 번호 입력: ")

            if action == '1':
                self.handle_sale()
            elif action == '2':
                self.handle_add_menu()
            elif action == '3':
                print("프로그램 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해 주세요.")

    def handle_sale(self):
        inventory_items = self.inventory.get_inventory()
        # 인벤토리가 비어있을 경우
        if not inventory_items:
            print("판매할 커피가 없습니다. 먼저 커피를 추가하세요.")
            return

        # 인벤토리에 있을 경우
        print("판매할 커피를 선택하세요")
        for index, (name, coffee) in enumerate(inventory_items.items()):
            print(f"{index}. {coffee.get_name()} {coffee.get_price()}원")

        choice = int(input("번호를 입력하세요: "))
        coffeeList = list(inventory_items.keys())
        selected_coffee = inventory_items[coffeeList[choice]]
        print(f"{selected_coffee.get_name()}가 판매되었습니다. 가격은 {selected_coffee.get_price()}입니다.")


    def handle_add_menu(self):
        coffeeName = input("커피 이름: ")
        coffeePrice = int(input("커피 가격: "))
        self.inventory.add_coffee(Coffee(coffeeName, coffeePrice))
        print(f"{coffeeName}가 메뉴에 추가되었습니다.")



