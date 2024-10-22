class OrderManager:
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id, order_data):
        if order_id not in self.orders:
            self.orders[order_id] = order_data
            print(f'Заказ с ID {order_id} добавлен')
        else:
            print(f'Заказ с ID {order_id} уже существует')

    def update_order(self, order_id, order_data):
        if order_id in self.orders:
            self.orders[order_id].update(order_data)
            print(f'Заказ с ID {order_id} обнавлён')
        else:
            print(f'Заказ с ID <{order_id} не найден')

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print(f'Заказ с ID {order_id} удалён')
        else:
            print(f'Заказ с ID <{order_id} не найден')
