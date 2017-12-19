from ProductList import ProductList
from DeliveryModule import DeliveryModule
from ApiExtender import APIExtender
from Supermarket import SuperMarket
from StatisticsCollector import StatisticsCollector
from Notification import Notification


class Fridge:
    def __init__(self):
        self._availableProducts = ProductList()
        self._movableModule = DeliveryModule()
        self._owner = None
        self._apiExtender = APIExtender()
        self._statCollector = StatisticsCollector()

    def notify_owner(self, event):
        notification = Notification();
        notification.notify()

    def buy_food_from_supermarket(self, supermarket_id):
        food = self._calc_needed_food()
        prod_list = SuperMarket(supermarket_id).buy_food(food)
        Notification.notify_user(self._owner)
        if prod_list:
            self._statCollector.add_bought_products(prod_list)
            return True
        else:
            return False

    def _calc_needed_food(self):
        # ... calc somehow
        return None

    def show_statistics(self):
        return self._statCollector.show_statistics();

    def show_receipts(self):
        receipts = None
        # calc receipts somehow
        Notification().notify_user(self._owner)
        return receipts

    def deliver_food_to_owner(self, products):
        self._movableModule.deliver_food(products)
        self._statCollector.add_consumed_product(products)
        return True

    def extend_api(self, path_to_module):
        self._apiExtender.load_module(path_to_module)

