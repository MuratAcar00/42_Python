#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._age_days = age_days if age_days >= 0 else 0

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, new_height: float) -> bool:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = new_height
        return True

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age_days = new_age
        return True

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    if rose.set_height(25.0):
        print("Height updated: 25cm")
    if rose.set_age(30):
        print("Age updated: 30 days")
    print()

    if not rose.set_height(-5.0):
        print("Height update rejected")
    if not rose.set_age(-10):
        print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()
