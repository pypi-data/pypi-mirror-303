from online_store.order_management import OrderManager
from online_store.user_management import UserManager


def main_menu():
    user_manager = UserManager()
    order_manager = OrderManager()

    while True:
        print('\nВыберите действие:')
        print('1. Управление учётными записями клиентов')
        print('2. Управление заказами')
        print('3. Выход')

        choice = input('Введите номер действия: ')

        if choice == '1':
            user_menu(user_manager)
        elif choice == '2':
            order_menu(order_manager)
        elif choice == '3':
            print('Работа завершена.')
            break
        else:
            print('Некорректный ввод. Попробуйте снова.')


def user_menu(user_manager):
    while True:
        print('\nУправление учётными записями клиентов:')
        print('1. Добавить учётную запись')
        print('2. Найти учётную запись')
        print('3. Удалить учётную запись')
        print('4. Назад')

        choice = input('Выберите действие: ')

        if choice == '1':
            user_id = input('Введите email клиента: ')
            name = input('Введите имя: ')
            age_input = input('Введите возраст: ')
            try:
                age = int(age_input)
                user_manager.add_user(user_id, {'name': name, 'age': age})
            except ValueError:
                print('Возраст должен быть числом.')
        elif choice == '2':
            user_id = input('Введите email клиента: ')
            user = user_manager.find_user(user_id)
            if user:
                print(user)
        elif choice == '3':
            user_id = input('Введите email клиента: ')
            user_manager.remove_user(user_id)
        elif choice == '4':
            break
        else:
            print('Некорректный ввод.')


def order_menu(order_manager):
    while True:
        print('\nУправление заказами:')
        print('1. Создать заказ')
        print('2. Обновить заказ')
        print('3. Отменить заказ')
        print('4. Назад')

        choice = input('Выберите действие: ')

        if choice == '1':
            order_id = input('Введите ID заказа: ')
            user = input('Введите email клиента: ')
            item = input('Введите товар: ')
            price_input = input('Введите цену: ')
            try:
                price = float(price_input)
                order_manager.create_order(order_id, {'user': user, 'item': item, 'price': price})
            except ValueError:
                print('Цена должна быть числом.')
        elif choice == '2':
            order_id = input('Введите ID заказа: ')
            status = input('Введите статус: ')
            order_manager.update_order(order_id, {'status': status})
        elif choice == '3':
            order_id = input('Введите ID заказа: ')
            order_manager.cancel_order(order_id)
        elif choice == '4':
            break
        else:
            print('Некорректный ввод.')


if __name__ == '__main__':
    main_menu()
