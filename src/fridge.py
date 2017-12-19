from ProductList import ProductList
from MovableModule import MovableModule

class Fridge:
    def __init__(self):
        self._availableProducts = ProductList()
        self._movableModule = MovableModule()
        self._owner = None
        pass

    def notify_owner(self)  :
        pass

    def buy_food_from_supermarket(self):
        pass

    def show_statistics(self):
        pass

    def show_receipts(self):
        pass

    def deliver_food_to_owner(self):
        self._movableModule.deliver_food()
        pass
