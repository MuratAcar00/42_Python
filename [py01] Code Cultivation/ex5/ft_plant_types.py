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


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
