# Inventory 클래스
# item 속성
# add_coffee(coffee) [item에 넣어주는 역할]
# get_inventory [item을 돌려주는 역할]

class Inventory:
    def __init__(self):
        self.items = {}

    def add_coffee(self, coffee):
        self.items[coffee.get_name()] = coffee

    def get_inventory(self):
        return self.items

