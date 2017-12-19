from src.ProductList import ProductList


class MovableModule:
    def __init__(self):
        self._loadedFood = ProductList()
        self._owner = None
        pass

    def move_to_owner(self):
        pass

    def deliver_food(self):
        pass

    def give_food(self, food):
        pass

    def get_back(self):
        pass