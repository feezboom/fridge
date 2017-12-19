from fridge import Fridge

class User:
    def __init__(self):
        self._location = None
        self._timetable = None
        self._preferences = None
        self._fridge = Fridge()
        pass

    def retrieve_food(self, products):
        pass

    def take_food_from_fridge(self, products):
        self._fridge.deliver_food_to_owner(products)

    def use_website_api(self, products):
        pass
