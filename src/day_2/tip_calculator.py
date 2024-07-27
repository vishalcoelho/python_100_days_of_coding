def tip_calculator() -> float:
    """Split a bill, including tip, among a desired number of people."""
    print("Welcome to the Tip Calculator!")
    total_bill = float(input("What was the total bill?"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
    n_people = int(input("How many people to split the bill?"))

    bill_per_head = round(total_bill / n_people * (1.0 + tip / 100.0), 2)
    print(f"Each person should pay: ${bill_per_head:4.2f}")
    return bill_per_head


if __name__ == "__main__":
    tip_calculator()
