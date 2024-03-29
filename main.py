class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id  # уникальный идентификатор пользователя
        self._name = name  # имя пользователя
        self._access_level = access_level  # уровень доступа, по умолчанию 'user'

    def get_user_id(self):
        return self._user_id  # предоставляет доступ, возвращает идентификатор пользователя

    def get_name(self):
        return self._name  # предоставляет доступ, возвращает имя пользователя

    def set_name(self, new_name):
        self._name = new_name  # предоставляет доступ и устанавливает новое имя пользователя

    def get_access_level(self):
        return self._access_level  #  предоставляет доступ и возвращает уровень доступа пользователя

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')  # вызов конструктора базового класса с уровнем доступа 'admin'
        self.__users_list = []  # список для хранения объектов пользователей

    def add_user(self, user):
        self.__users_list.append(user)  # добавление пользователя в список
        print(f"Пользователь {user.get_name()} добавлен.")  # уведомление о добавлении пользователя

    def remove_user(self, user_id):
        user_to_remove = None
        for user in self.__users_list:  # поиск пользователя по идентификатору
            if user.get_user_id() == user_id:
                user_to_remove = user
                break
        if user_to_remove:
            self.__users_list.remove(user_to_remove)  # удаление пользователя из списка
            print(f"Пользователь {user_to_remove.get_name()} удален.")  # уведомление о удалении
        else:
            print("Пользователь не найден.")  # сообщение, если пользователь не найден


# Пример использования
if __name__ == "__main__":
    admin = Admin(1, "Виктор")  # Создание администратора
    user1 = User(2, "Петя")  # Создание обычного пользователя
    user2 = User(3, "Иван")  # Создание еще одного обычного пользователя
    user3 = User(4, "Сергей")  # Создание еще одного обычного пользователя

    admin.add_user(user1)  # Администратор добавляет пользователя user1
    admin.add_user(user2)  # Администратор добавляет пользователя user2
    admin.add_user(user3)  # Администратор добавляет пользователя user3


    print(f"Имя админа {admin.get_name()}.")
    print(f'у админа уровень доступа - {admin.get_access_level()}')  # Получение уровня доступа админа ('admin')
    print(f'у Пети уровень доступа - {user1.get_access_level()}')  # Получение уровня доступа пользователя user1 ('user')

    admin.remove_user(3)  # Администратор удаляет пользователя с ID 2

    user3.set_name("Алексей")
    print(f"Новое имя  пользователя под номером 3 - {user3.get_name()}. Встречайте!")