from abc import ABC, abstractmethod

class NotMatchLeague(Exception):
    pass

class Player(ABC):
    age_limit: tuple[int, int]

    @abstractmethod
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError(f'Age must be int, not {type(new_age).__name__}')
        if not (self.age_limit[0] <= new_age <= self.age_limit[1]):
            raise NotMatchLeague(f"You're age is not match this League, you're age is {new_age}")
        self._age = new_age

    def __str__(self) -> str:
        return f'{self.__class__.__name__} name: {self.name}, age: {self.age}'

    def __eq__(self, other) -> bool:
        return self.age == other.age

    def __ne__(self, other) -> bool:
        return self.age != other.age

    def __le__(self, other) -> bool:
        return self.age <= other.age

    def __lt__(self, other) -> bool:
        return self.age < other.age

    def __ge__(self, other) -> bool:
        return self.age >= other.age

    def __gt__(self, other) -> bool:
        return self.age > other.age


class SchoolLeaguePlayer(Player):
    age_limit = (11, 13)
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)


im = SchoolLeaguePlayer('Maria', 11)
you = SchoolLeaguePlayer('Nastya', 12)
print(im.__str__())
print(im != you)
print(you.__str__())
