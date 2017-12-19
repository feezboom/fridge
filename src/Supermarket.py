from ProductList import ProductList
from ProductCatalog import ProductCatalog
from Food import Food


class SuperMarket:
    def __init__(self, id):
        self._productCatalog = ProductCatalog()
        self._id = id
        pass

    def buy_food(self, product_list):
        return ProductList()

    def get_product_catalog(self):
        return ProductCatalog()

