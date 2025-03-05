import csv

def load_exchange_rates(filename): # this will load exchange rates from the currency.csv file given by the professor
    exchange_rates = {}
    try:
        with open(filename, mode="r", encoding="latin-1") as file:  
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if len(row) != 3:  # this ensures the 3 columns (code, name, rate) in the csv file
                    print(f"Skipping invalid row: {row}")
                    continue
                currency_code = row[0].strip().upper()  # this is for the first column (Code)
                try:
                    rate = float(row[2].strip())  # this is for the third column (Rate)
                    exchange_rates[currency_code] = rate
                except ValueError:
                    print(f"Skipping row with invalid number format: {row}")
    except FileNotFoundError:
        print("Error: 'currency.csv' not found.")
        return None
    return exchange_rates

# this converts the initial value of USD to the target currency depending on the user's needs
def convert_currency(usd_amount, target_currency, exchange_rates):
    if target_currency in exchange_rates:
        return usd_amount * exchange_rates[target_currency]
    else:
        print(f"Error: '{target_currency}' not found in exchange rates.")
        return None

# main program!!!
def main():
    filename = "currency.csv"
    print("\nOpening and reading currency exchange file...\n") # the system will prompt this message for processing purposes
    exchange_rates = load_exchange_rates(filename)

    if exchange_rates is None:
        return

    print("Available Currencies:", ", ".join(exchange_rates.keys()))

    try:
        usd_amount = float(input("\nHow much dollar do you have? "))
    except ValueError:
        print("Invalid dollar amount!")
        return

    target_currency = input("What currency do you want to have? ").strip().upper()
    converted_amount = convert_currency(usd_amount, target_currency, exchange_rates)

    if converted_amount is not None:
        print(f"\nDollar: {usd_amount} USD")
        print(f"{target_currency}: {converted_amount:.6f}")

if __name__ == "__main__":
    main()
