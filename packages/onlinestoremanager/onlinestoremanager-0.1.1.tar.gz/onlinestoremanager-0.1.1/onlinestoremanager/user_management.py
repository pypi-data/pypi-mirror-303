class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_data):
        if user_id not in self.users.keys():
            self.users[user_id] = user_data
            print(f'Клиент с ID {user_id} добавлен')
        else:
            print(f'Клиент с ID {user_id} уже существует')

    def remove_user(self, user_id):
        if user_id in self.users.keys():
            del self.users[user_id]
            print(f'Клиент с ID {user_id} удалён')
        else:
            print(f'Клиент с ID {user_id} не существует')

    def update_user(self, user_id, user_data):
        if user_id in self.users.keys():
            self.users[user_id].update(user_data)
            print(f'Клиент с ID {user_id} обнавлён')
        else:
            print(f'Клиент с ID {user_id} не существует')

    def find_user(self, user_id):
        if user_id in self.users.keys():
            return self.users[user_id]
        else:
            return f'Клиент с ID {user_id} не существует'