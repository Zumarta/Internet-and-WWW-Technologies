import sys
import json


# Arithmetic encoding of the given argument string
def main():
    # DEBUG
    # input_json = json.loads("{\"probabilities\": { \"H\": 0.3333333333333333, \"I\": 0.3333333333333333, \"P\": 0.3333333333333333 },  \"data\": 0.2777777777777778, \"length\": 3, \"interval\": [0.0, 1.0]}")

    # read input file
    input_json = json.load(sys.stdin)

    # Extract data from given json
    probs = input_json["probabilities"]
    code = input_json["data"]
    length = input_json["length"]
    start = input_json["interval"][0]
    end = input_json["interval"][1]

    # Decode code
    encoded_string = decode(code, probs, length, start, end)

    # print decoded string
    print(encoded_string)


# Decodes the given code with its probabilities and expected string length
def decode(code, probs, length, start, end):
    encoded_string = ""

    while True:
        # Initial
        lower, upper = 0, 1
        # Get intervals in which we are
        for k, prob in probs.items():
            # Get basic probability ranges
            upper = lower + prob

            # helper to store value unchanged
            b = start
            cur_start = b + lower * (end - b)
            cur_end = b + upper * (end - b)

            if cur_start <= code <= cur_end:
                encoded_string += k
                start = cur_start
                end = cur_end
                break
            else:
                # Set lower "one step further"
                lower += prob

        # Break if we are finished
        if len(encoded_string) >= length:
            break

    return encoded_string


main()
