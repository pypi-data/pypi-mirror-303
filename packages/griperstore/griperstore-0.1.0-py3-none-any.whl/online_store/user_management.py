class UserManager:
    def __init__(self):
        # Инициализация атрибута — словарь для хранения учетных записей
        self.users = {}

    def add_user(self, user_id, user_data):
        # Добавление нового пользователя
        if user_id in self.users:
            return f'Клиент с ID {user_id} уже существует.'
        self.users[user_id] = user_data
        return f'Клиент с ID {user_id} добавлен.'

    def remove_user(self, user_id):
        # Удаление пользователя
        if user_id not in self.users:
            return f'Клиент с ID {user_id} не найден.'
        del self.users[user_id]
        return f'Клиент с ID {user_id} удален.'

    def update_user(self, user_id, user_data):
        # Обновление данных пользователя
        if user_id not in self.users:
            return f'Клиент с ID {user_id} не найден.'
        self.users[user_id].update(user_data)
        return f'Данные клиента с ID {user_id} обновлены.'

    def find_user(self, user_id):
        # Поиск пользователя по ID
        if user_id not in self.users:
            return f'Клиент с ID {user_id} не найден.'
        return self.users[user_id]


# Пример использования
if __name__ == "__main__":
    manager = UserManager()

    # Добавление нового клиента
    print(manager.add_user('user1@example.com', {'name': 'John Doe', 'age': 30}))

    # Обновление данных клиента
    print(manager.update_user('user1@example.com', {'age': 31}))

    # Поиск клиента
    print(manager.find_user('user1@example.com'))

    # Удаление клиента
    print(manager.remove_user('user1@example.com'))

    # Поиск удалённого клиента
    print(manager.find_user('user1@example.com'))