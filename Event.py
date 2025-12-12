from datetime import datetime

from Bron import Bron
from DBManager import DBManager


class Event():
    def __init__(self, title: str,
                 description: str,
                 date: datetime,
                 count: int,
                 price: float,
                 location: str,
                 manager: DBManager):

        self.title = title
        self.description = description
        self.date = date
        self.count = count
        self.price = price
        self.location = location
        self.broni = []
        self.manager = manager

        self.manager.add_event(self.title, self.description, self.date, self.count, self.price, self.location)



    def add_bron(self, id:int, name:str, n: int) -> None:
        tmp = self._count_bilets()
        if tmp < n:
            print(f"нет свободных мест(осталось {tmp} мест)")
            return

        self.broni.append(Bron(name ,n))
        self.manager.add_broni(id, self.broni[-1])
        print(f"Ваша бронь записана, осталось мест: {tmp - n}")
        print(f"Стоимость ваших билетов: {self.price * n}")

        return


    def _count_bilets(self):
        tmp = 0
        for i in self.broni:
            tmp += i.count
        return self.count - tmp


    def show_bron(self):
        for i in self.broni:
            i.show()

    def show(self):
        print("_"*50)
        print(f"'{self.title}' - пройдёт {self.date} в {self.location}")
        print(f"Осталось {self.count} билетов по {self.price} рублей.")
        print("_"*50)

    def __str__(self):
        return f"{self.title} - {self.date} - {self.location}"




