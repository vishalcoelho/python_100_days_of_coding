def generate_band_name() -> str:
    """Generates and returns a band name formed from multiple user name."""
    print("Welcome to the Band Name Generator.")
    city_name = input("What is the name of the city you grew up in?")
    pet_name = input("What is your pet's name? ")
    band_name = city_name + " " + pet_name
    print(f"Your band name could be {band_name}")
    return band_name


if __name__ == "__main__":
    generate_band_name()
