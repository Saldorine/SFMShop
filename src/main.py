from src.models.order import Order
from src.models.user import User
from src.models.product import Product
from src.models.payment import CardPayment, PayPalPayment
from src.models.exceptions import ValidationError, BusinessLogicError, DataTypeError

def process_order_system():
    try:
        user = User('Иван', 'ivan@test.ru')
    except ValidationError as e:
        print('Ошибка валидации:', e)

    try:
        product1 = Product('Ноутбук', 50000, 2)
        product2 = Product('Мышь', 1500, 3)
    except ValidationError as e:
        print('Ошибка валидации:', e)

    try:
        order = Order(user, [product1, product2])
        total = order.calculate_total()
        print("Общая стоимость заказа:", total)
    except BusinessLogicError as e:
        print('Ошибка бизнес логики:', e)
    except DataTypeError as e:
        print('Ошибка типа данных:', e)

    payments = [
        CardPayment(1000, "1234 5678 9012 3456"),
        PayPalPayment(2000, "test@paypal.com")
    ]

    for payment in payments:
        print(payment.process_payment())

    sorted_products = sorted([product1, product2])
    for product in sorted_products:
        print(product)

    #Обработка ошибок
    try:
        user = User('Иван', 'ivantest.ru')
    except ValidationError as e:
        print('Ошибка валидации:', e)

    try:
        product1 = Product('Ноутбук', -50000, 2)
        product2 = Product('Мышь', 1500, 3)
    except ValidationError as e:
        print('Ошибка валидации:', e)

    try:
        order = Order(user, [])
        total = order.calculate_total()
        print("Общая стоимость заказа:", total)
    except BusinessLogicError as e:
        print('Ошибка бизнес логики:', e)
    except DataTypeError as e:
        print('Ошибка типа данных:', e)



process_order_system()