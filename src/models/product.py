from src.models.exceptions import NegativePriceError, InsufficientStockError


class Product:
    def __init__(self, name, price, quantity):
        self.price = 0
        self.name = name
        self.quantity = quantity
        self.set_price(price)


    def sell(self, amount):
        if self.quantity < amount:
            raise InsufficientStockError(
                f"Товара недостаточно. На складе: {self.quantity}, требуется: {amount}"
            )
        self.quantity = self.quantity - amount


    def set_price(self, price):
        if price < 0:
            raise NegativePriceError('Цена не может быть отрицательной')
        self.price = price


    def get_total_price(self):
        return self.price * self.quantity


    def __str__(self):
        return f'Товар: {self.name}, Цена: {self.price} руб., Количество: {self.quantity}'


    def __repr__(self):
        return f'Product(\'{self.name}\', {self.price}, {self.quantity})'


    def __lt__(self, other):
        return self.price < other.price


    def __eq__(self, other):
        return self.price == other.price and self.name == other.name


    def check_stock(self):
        pass


    def update_stock(self):
        pass

    def calculate_shipping(self):
        pass