class Bird:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

    def fly(self):
        print(f"{self.name}(이)가 날아오릅니다.")

    def lay(self):
        print(f"{self.name}(이)가 알을 낳습니다.")

class Flyable:
    def fly(self):
        print("날아 다닙니다.")

class Eagel(Bird, Flyable):
    def crawl(self):
        print(f"{self.name}(이)가 사냥합니다.")

class Penguin(Bird):
    def swim(self):
        print(f"{self.name}(이)가 수영합니다.")


