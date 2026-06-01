#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def grow(self, amount: float) -> None:
        self.height = round(self.height + amount, 1)

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30)
    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age()
        rose.show()

    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")
