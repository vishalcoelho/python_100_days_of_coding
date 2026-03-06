"""Show how modules are imported and used."""

from prettytable import PrettyTable


def main():
    """Demonstrate how to create an object"""
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charamander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])

    # Change attributes
    table.align = r"l"

    print(table)


if __name__ == "__main__":
    main()
