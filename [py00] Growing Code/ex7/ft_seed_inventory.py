def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seedName = seed_type.capitalize()

    if unit == "packets":
        print(f"{seedName} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seedName} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seedName} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
