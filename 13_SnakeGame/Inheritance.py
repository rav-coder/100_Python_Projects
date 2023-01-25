class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("underwater")

    def swim(self):
        print("swimming")