from Food import Food

class ProductList:
    def __init__(self):
        self._products = []
        self._prices = []
        pass

    def add_products(self, products):
        self._products.append(products)
