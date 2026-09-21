def expense_tracker():
    # Initialize the total spent accumulator
    total_spent = 0.0

    print("=== EXPENSE TRACKER ===")
    print("Enter your expenses one by one. Type 'done' or '0' to finish.\n")

    while True:
        user_input = input("Enter expense amount: ").strip()

        # Check for exit condition
        if user_input.lower() == "done" or user_input == "0":
            break

        try:
            # Convert user input to float for decimal values
            new_expense = float(user_input)

            if new_expense < 0:
                print("Please enter a positive amount.")
                continue

            # Accumulate total using accumulator pattern (total = total + new_expense)
            total_spent = total_spent + new_expense
            print(f"Added ${new_expense:.2f}. Current Total: ${total_spent:.2f}\n")

        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.\n")

    print("\n-------------------------")
    print(f"Total Spent: ${total_spent:.2f}")
    print("-------------------------")


if __name__ == "__main__":
    expense_tracker()