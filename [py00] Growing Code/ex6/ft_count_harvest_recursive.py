def ft_count_harvest_recursive() -> None:
    targetDay = int(input("Days until harvest: "))

    def helperCounter(currentDay: int, target: int) -> None:
        if currentDay > target:
            print("Harvest Time")
            return

        print(f"Day {currentDay}")
        helperCounter(currentDay + 1, target)

    helperCounter(1, targetDay)
