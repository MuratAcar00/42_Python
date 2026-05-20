def ft_water_reminder() -> None:
    days_since_watering = int(input("ft_water_reminder: "))
    if days_since_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
