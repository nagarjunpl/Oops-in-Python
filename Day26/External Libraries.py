from currency_converter import CurrencyConverter

a = CurrencyConverter()

amt = float(input("Enter the amount: "))  # user input for amount

from_currency = input("Enter the from currency (e.g., USD): ").upper()  # convert to uppercase
to_currency = input("Enter the to currency (e.g., INR): ").upper()      # convert to uppercase

# Corrected line: pass the variables, not string literals
conversion = a.convert(amt, from_currency, to_currency)

print(f"Converted amount from {from_currency} to {to_currency} is: {conversion:.2f}")
