class OrderManager:
    def __init__(self):
        # Инициализация словаря для хранения заказов
        self.orders = {}

    def create_order(self, order_id, order_data):
        if order_id in self.orders:
            print(f'Заказ с ID {order_id} уже существует')
        else:
            self.orders[order_id] = order_data
            print(f'Заказ с ID {order_id} добавлен')

    def update_order(self, order_id, order_data):
        if order_id in self.orders:
            self.orders[order_id].update(order_data)
            print(f'Заказ с ID {order_id} обновлён')
        else:
            print(f'Заказ с ID {order_id} не найден')

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print(f'Заказ с ID {order_id} отменён')
        else:
            print(f'Заказ с ID {order_id} не найден')
