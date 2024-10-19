class OrderManager:
    def __init__(self):
           # Добавь инициализацию атрибута — словаря для хранения заказов.
        self.orders = {}
           
    def create_order(self, order_id, **order_data):
           # Добавь логику создания заказа.
           # Когда заказ обновлён, выведи сообщение 'Заказ с ID <order_id> обновлён'.
           # Если заказ с таким ID уже существует, создавать его заново не нужно. Выведи сообщение 'Заказ с ID <order_id> уже существует'.
        order = self.orders.get(order_id)
        if order:
            print(f'Заказ с ID {order_id} уже существует')
        else:
            self.orders[order_id] = order_data
            print(f'Заказ с ID {order_id} добавлен')

    def update_order(self, order_id, **order_data):
           # Добавь логику обновления заказа — выведи соответствующее сообщение.
           # Когда заказ создан, выведи сообщение 'Заказ с ID <order_id> добавлен'.
           # Если заказа не существует, выведи сообщение 'Заказ с ID <order_id> не найден'.
        order = self.orders.get(order_id)
        if order:
            self.orders[order_id].update(order_data)
            print(f'Заказ с ID {order_id} обновлен')
        else:
            print(f'Заказ с ID {order_id} не найден')

    def cancel_order(self, order_id):
           # Добавь логику отмены заказа.
           # Когда заказ создан, выведи сообщение 'Заказ с ID <order_id> отменён'.
           # Если заказа не существует, выведи сообщение 'Заказ с ID <order_id> не найден'.
        order = self.orders.get(order_id)
        if order:
            del self.orders[order_id]
            print(f'Заказ с ID {order_id} отменён')
        else:
            print(f'Заказ с ID {order_id} не найден')