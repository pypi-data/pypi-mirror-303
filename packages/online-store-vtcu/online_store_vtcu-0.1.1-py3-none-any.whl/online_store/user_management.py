class UserManager:
    def __init__(self):
        # Инициализация словаря для хранения учётных записей клиентов
        self.users = {}

    def add_user(self, user_id, user_data):
        if user_id in self.users:
            print(f'Клиент с ID {user_id} уже существует')
        else:
            self.users[user_id] = user_data
            print(f'Клиент с ID {user_id} добавлен')

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f'Клиент с ID {user_id} удалён')
        else:
            print(f'Клиент с ID {user_id} не найден')

    def update_user(self, user_id, user_data):
        if user_id in self.users:
            self.users[user_id].update(user_data)
            print(f'Данные клиента с ID {user_id} обновлены')
        else:
            print(f'Клиент с ID {user_id} не найден')

    def find_user(self, user_id):
        if user_id in self.users:
            return self.users[user_id]
        else:
            print(f'Клиент с ID {user_id} не найден')
            return None
