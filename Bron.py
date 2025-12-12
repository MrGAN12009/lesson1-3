from dataclasses import dataclass

@dataclass
class Bron:
    name: str
    count: int

    def show(self):
        print(f"+{'-'*50}+")
        print(f"|На имя:{' '*(43 - len(self.name))}{self.name}|")
        print(f"|Стоимость:{' '*(40 - len(str(self.count)))}{self.count}|")
        print(f"+{'-'*50}+")