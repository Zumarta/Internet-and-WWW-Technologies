import argparse


# Task: Mit Argparse Zahlen aufaddieren
# Mit Option soll man dann auch multiplizieren können
parser = argparse.ArgumentParser(description='Sum or multiply integers.')

# Metavar just shows another name
# nargs="+" expects at least one parameter
parser.add_argument('numbers', metavar='N', nargs='+', type=int, help='Integers to accumulate')

# store_true: save true to isMultiply, if --multiply has been set
parser.add_argument('--multiply', action='store_true', help='Multiply values (default: sum them)')

# Parse arguments
args = parser.parse_args()

# Set result initially to 1 if its multiplication to avoid multiplying with 0
result = 1 if args.multiply else 0

for n in args.numbers:
    if args.multiply:
        result *= n
    else:
        result += n

print(result)