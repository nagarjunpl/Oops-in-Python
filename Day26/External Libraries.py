# Currency Converter using an external library

from currency_converter import CurrencyConverter

a = CurrencyConverter()

amt = float(input("Enter the amount: "))  # user input for amount

from_currency = input("Enter the from currency (e.g., USD): ").upper()  # convert to uppercase
to_currency = input("Enter the to currency (e.g., INR): ").upper()      # convert to uppercase

# Corrected line: pass the variables, not string literals
conversion = a.convert(amt, from_currency, to_currency)

print(f"Converted amount from {from_currency} to {to_currency} is: {conversion:.2f}")


# Currency Converter with specifc date

from currency_converter import CurrencyConverter
from datetime import date  # Correct import for date

a = CurrencyConverter()

amt = float(input("Enter the amount: "))  # user input for amount

from_currency = input("Enter the from currency (e.g., USD): ").upper()  # convert to uppercase
to_currency = input("Enter the to currency (e.g., INR): ").upper()      # convert to uppercase

# Use date from datetime module
conversion = a.convert(amt, from_currency, to_currency, date=date(2020, 1, 3))

print(f"Converted amount from {from_currency} to {to_currency} on 2020-01-01 is: {conversion:.3f}")
