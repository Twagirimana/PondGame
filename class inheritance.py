class Food:
    def __init__(self):
        self.color = "white"

    def cook(self):
        print("they are cooking me")


class Rice(Food):
    def __init__(self):
        super().__init__()

    def size(self):
        super().__init__()
        print("small")

    def cook(self):
        super().cook()
        print("with water")


name = Rice()
print(name.color)
name.size()
name.cook()
