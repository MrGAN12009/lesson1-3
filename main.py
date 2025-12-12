from DBManager import DBManager
from Event import Event
from datetime import datetime


def menu():
    try:
        print("Система бронирования")
        print("Выберите:")
        print("1. Добавить бронь. ")
        print("2. Посмотреть брони. ")
        print("3. посмотреть мероприятие. ")
        print("4. Добавление мероприятия. ")
        print("5. Общий список мероприятий. ")
        return int(input("Введите выбор: "))
    except ValueError:
        print("---ВВедите целое число!!!")
        return menu()

def main():
    manager = DBManager()
    events = [Event(f"title_event{i}", f"descripe_{i}", datetime.now(), 100*i, 1000*i, "Москва", manager) for i in range(1, 6)]


    while True:
        choice = menu()
        if choice == 1:
            id = int(input("Ведите id мероприятия: "))
            name = input("Введите имя брони: ")
            count = int(input("Введите колчиество билетов для брони: "))
            events[id].add_bron(id, name, count)
        elif choice == 2:
            events[int(input("Ведите id мероприятия: "))].show_bron()
        elif choice == 3:
            events[int(input("Ведите id мероприятия: "))].show()
        elif choice == 4:
            title = input("Введите название мероприятия: ")
            description = input("Введите описание мероприятия: ")
            date = datetime.now()
            count = int(input("Введите количество мест на мероприятии: "))
            price = int(input("Введите стоимость билета на мероприятие: "))
            location = input("Введите локацию мероприятия: ")
            events.append(Event(title, description, date, count, price, location))
        elif choice == 5:
            for event in events:
                print(event.__str__())
        else:
            continue


if __name__ == "__main__":
    main()