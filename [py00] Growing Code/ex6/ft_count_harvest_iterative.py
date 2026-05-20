def ft_count_harvest_iterative() -> None:
    targetDay = int(input("Days until harvest: "))
    for i in range(1, targetDay + 1):
        print("Day ", i)
    print("Harvest time!")
