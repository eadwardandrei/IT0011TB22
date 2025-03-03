import csv

# Load currency exchange rates from the CSV file
def load_exchange_rates(filename):
    exchange_rates = {}
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            currency, rate = row
            exchange_rates[currency.strip()] = float(rate)
    return exchange_rates

# Function to convert USD to the chosen currency
def convert_currency(usd_amount, target_currency, exchange_rates):
    if target_currency in exchange_rates:
        converted_amount = usd_amount * exchange_rates[target_currency]
        return converted_amount
    else:
        return None  # Currency not found

# Main program
def main():
    filename = "currency.csv"  # Ensure the file is in the same directory
    exchange_rates = load_exchange_rates(filename)

    # User input
    usd_amount = float(input("How much dollar do you have? "))
    target_currency = input("What currency you want to have? ").strip().upper()

    # Conversion
    converted_amount = convert_currency(usd_amount, target_currency, exchange_rates)

    # Output result
    if converted_amount is not None:
        print(f"\nDollar: {usd_amount} USD")
        print(f"{target_currency}: {converted_amount:.6f}")
    else:
        print("Currency not found in the exchange rates.")

# Run the program
if __name__ == "__main__":
    main()
