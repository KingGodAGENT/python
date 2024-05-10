class Coffee():
    def __init__(self,a,b,c):
        self.name = a
        self.price = b
        self.caffein = c

    def intro(self):
        return f"{self.caffein} {self.name} {self.price}원"

    def nameFixed(self, a):
        self.name = a