class OrderManager:
    def __init__(self):
        # Инициализация атрибута — словарь для хранения заказов
        self.orders = {}

    def create_order(self, order_id, order_data):
        # Создание нового заказа
        if order_id in self.orders:
            return f'Заказ с ID {order_id} уже существует.'
        self.orders[order_id] = order_data
        return f'Заказ с ID {order_id} добавлен.'

    def update_order(self, order_id, order_data):
        # Обновление данных заказа
        if order_id not in self.orders:
            return f'Заказ с ID {order_id} не найден.'
        self.orders[order_id].update(order_data)
        return f'Данные заказа с ID {order_id} обновлены.'

    def cancel_order(self, order_id):
        # Отмена заказа
        if order_id not in self.orders:
            return f'Заказ с ID {order_id} не найден.'
        del self.orders[order_id]
        return f'Заказ с ID {order_id} отменён.'


# Пример использования
if __name__ == "__main__":
    order_manager = OrderManager()

    # Создание нового заказа
    print(order_manager.create_order('order1001', {'user': 'Alice', 'item': 'Smartphone', 'price': 799}))

    # Обновление данных заказа
    print(order_manager.update_order('order1001', {'status': 'shipped'}))

    # Отмена заказа
    print(order_manager.cancel_order('order1001'))