class UserManager:
       def __init__(self):
           self.users = {}

       def add_user(self, user_id, **user_data):
           # Добавь логику создания учётной записи.
           # Когда учётная запись создана, выведи сообщение 'Клиент с ID <user_id> добавлен'.
           # Если учётная запись уже существует, создавать её заново не нужно, необходимо вывести сообщение 'Клиент с ID <user_id> уже существует'.
           user = self.users.get(user_id)
           if user:
               print(f'Клиент с ID {user_id} уже существует')
           else:
               self.users[user_id] = user_data
               print(f'Клиент с ID {user_id} добавлен')
       def remove_user(self, user_id):
           # Добавь логику удаления учётной записи.
           # Когда учётная запись удалена, выведи сообщение 'Клиент с ID <user_id> удалён'.
           # Если учётной записи не существует, выведи сообщение 'Клиент с ID <user_id> не найден'.
           user = self.users.get(user_id)
           if user:
               del self.users[user_id]
               print(f'Клиент с ID {user_id} удалён')
           else:
               print(f'Клиент с ID {user_id} не найден')

       def update_user(self, user_id, **user_data):
           # Добавь логику обновления данных клиента.
           # Когда данные о клиенте обновлены, выведи сообщение 'Данные клиента с ID <user_id> обновлены'.
           # Если учётной записи не существует, выведи сообщение 'Клиент с ID <user_id> не найден'.
           user = self.users.get(user_id)
           if user:
               self.users[user_id] = user_data
               print(f'Данные клиента с ID {user_id} обновлены')
           else:
               print(f'Клиент с ID {user_id} не найден')

       def find_user(self, user_id):
           # Добавь логику поиска учётной записи.
           # Верни словарь с данными клиента, если он найден.
           # Если учётной записи не существует, выведи сообщение 'Клиент с ID <user_id> не найден'.
           user = self.users.get(user_id)
           if user:
               return user
           else:
               print(f'Клиент с ID {user_id} не найден')