#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def inc_grow(self) -> None:
            self._grow_calls += 1

        def inc_age(self) -> None:
            self._age_calls += 1

        def inc_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.stats = self._Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self.stats.inc_show()
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def grow(self, amount: float) -> None:
        self.stats.inc_grow()
        self.height = round(self.height + amount, 1)

    def age(self, amount: int = 1) -> None:
        self.stats.inc_age()
        self.age_days += amount


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
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def inc_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
        self.stats = self._TreeStats()

    def produce_shade(self) -> None:
        if isinstance(self.stats, Tree._TreeStats):
            self.stats.inc_shade()
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

    def age(self, amount: int = 1) -> None:
        super().age(amount)
        self.nutritional_value += amount

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str
    ) -> None:
        super().__init__(name, height, age_days, color)
        self.seeds_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds_count}")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_a_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_a_year(400)}"
    )
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)
    print()

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_statistics(unknown)
