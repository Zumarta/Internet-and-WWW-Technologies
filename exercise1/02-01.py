import argparse
import json


def main():
    # Read arguments
    input_string = read_input()

    # Get string length
    length = len(input_string)

    # probability dictionary
    probs = calc_probabilities(input_string)

    # Encode string
    code = encode_string(input_string, probs)

    # Print result
    print(json.dumps(
        {"probabilities": probs,
         "data": code,
         "length": length,
         "interval": [0.0, 1.0]
         }, indent=4))


# Getting the command line arguments
def read_input():
    parser = argparse.ArgumentParser(description='Calculate arithmetic code')
    parser.add_argument('string', help='String to encode')
    args = parser.parse_args()

    return args.string


# Creating a dictionary containing all probabilities for each character
def calc_probabilities(input_string):
    # Create empty dict
    prob = {}

    # Sort it alphabetically
    input_string = ''.join(sorted(input_string))

    # Create a dictionary entry for each character in our string
    # Probability = Character occurrences / string length
    for c in input_string:
        char_occurences = input_string.count(c)
        prob[c] = char_occurences / len(input_string)

    return prob


# Calculate initial intervals for each character
# and iterate through formula for each character
def encode_string(input_string, probs):
    # Set start & end interval's initial values to [0,1)
    start, end = 0.0, 1.0

    for c in input_string:
        c_start_interval, c_end_interval = 0, 0

        # Approximate from 0 to the searched character and add interval to get the start interval
        for key in probs:
            if key == c:
                break
            else:
                c_start_interval += probs[key]

        # To get the end interval, add the c's probability to the start interval
        c_end_interval = c_start_interval + probs[c]

        # Temporary values to hold their values before rewriting them
        current_start, current_end = start, end

        # Get new start and end interval for this iteration
        start = current_start + ((current_end - current_start) * c_start_interval)
        end = current_start + ((current_end - current_start) * c_end_interval)

    # Get the middle value between our interval
    code = (start + end) / 2

    return code


# Call encoding
main()
