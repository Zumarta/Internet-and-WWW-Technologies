import argparse

# Helpful: https://de.wikipedia.org/wiki/Zyklische_Redundanzpr%C3%BCfung
def main():
    # FIXME
    # bitstring, polynomial = read_arguments()

    # Debug
    bitstring, polynomial = [1011010101110011], [1011]

    # TODO: outsource
    poly_degree = len(polynomial)

    # Fill bitstring with zeroes based on the polynomial degree
    for _ in polynomial:
        bitstring.append(0)


def read_arguments():
    """ Return bitstring and polynomial in its string format """
    parser = argparse.ArgumentParser(description='Sum or multiply integers.')

    parser.add_argument('bitstring', metavar='N', nargs='+', type=int, help='Bitstring')
    parser.add_argument('polynomial', metavar='N', nargs='+', type=int, help='Polynomial without leading zeroes')

    args = parser.parse_args()

    return args.bitstring, args.polynomial


if __name__ == '__main__':
    main()
