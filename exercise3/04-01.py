import argparse
import re


def main():
    # Get arguments
    bitstring, polynomial = read_arguments()

    # Perform CRC verification
    result = crc_check(bitstring, polynomial)

    if result == 0:
        exit(0)
    else:
        exit(25)


def read_arguments():
    """ Return bitstring and polynomial in its string format. """
    parser = argparse.ArgumentParser(description='Sum or multiply integers.')

    parser.add_argument('bitstring', metavar='N', nargs='+', type=int, help='Bitstring')
    parser.add_argument('polynomial', metavar='N', nargs='+', type=int, help='Polynomial without leading zeroes')

    args = parser.parse_args()

    # Parse lists to strings and remove brackets
    bitstring = str(args.bitstring).strip("[]")
    polynomial = str(args.polynomial).strip("[]")

    return bitstring, polynomial


def crc_check(bitstring, polynomial):
    """ Return 0 if the checksum was correct, otherwise return 25 """
    # RegEx pattern for a zero-check
    only_zeroes_pattern = re.compile("^[0]+$")

    rest = ""
    while len(bitstring) >= len(polynomial):
        i = 0
        while i < len(polynomial):
            if set(bitstring[i]) ^ set(polynomial[i]):
                rest += "1"
            else:
                rest += "0"

            i += 1

        # If our rest contains only zeroes and the bitstring length is equal to polynomial length, check was successful
        if only_zeroes_pattern.match(rest) and (len(bitstring) <= len(polynomial)):
            return 0

        # Reuse bitstring and cut off already checked bits
        bitstring = bitstring[len(polynomial):]

        # Delete leading zeroes
        rest = rest.lstrip("0")

        # Add not used part of bitstring to rest
        bitstring = rest + bitstring

        # Reset rest then
        rest = ""

    """ 
    If we arrive here, there has been a non-zero rest in our calculation and that said, 
    the message has not been delivered successfully 
    """
    return 25


if __name__ == '__main__':
    main()
