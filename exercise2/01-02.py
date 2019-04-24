from collections import OrderedDict
import json


# Arithmetic encoding of the given argument string
def main():
    # DEBUG
    input_json = json.loads(
        "{ \"dictionary\": { \"0000\": \"A\", \"0001\": \"B\", \"0010\": \"C\", \"0011\": \"D\" }, \"raw\": "
        "\"acdacdacbacbbacdd\"}")

    # In case of needed stdin reading
    # input_json = json.load(sys.stdin)

    # Extract data from given json
    # I use ordered dicts, because I'm lazy :)
    dictionary = OrderedDict(input_json["dictionary"])
    raw = input_json["raw"]

    compressed, dictionary = compress(raw, dictionary)

    # Prepare json output object
    output_obj = {
        "dictionary": dictionary,
        "compressed": compressed
    }

    json_output = json.dumps(output_obj, indent=4)

    # print encoded string
    print(json_output)


# Compress raw with LZW encoding with the help of the given dictionary
def compress(raw, dictionary):
    compressed = ""

    # Word length
    raw_length = len(raw)
    iteration = 0
    latest_char = ""  # Latest char is not set in the first iteration

    # Do it until we have used all characters
    while True:
        # Get current character as upper case letter
        current_char = raw[iteration].upper()
        combined_word = latest_char + current_char

        # If char is not in dict, append it to our dictionary, but do care about counting correctly!
        if combined_word not in dictionary.values():
            # Get the last entry to know where we have to count from
            last_entry_key = list(dictionary.keys())[-1]

            # Still lazy: Transform this number to decimal
            last_entry_key = int(last_entry_key, 2)

            # Increment it by one
            last_entry_key += 1

            # Convert it back to binary and use it as the next dictionary entry
            last_entry_key = format(last_entry_key, 'b')
            # We want to have 4 bit, otherwise codes start with other code words
            if len(last_entry_key) <= 3:
                last_entry_key = last_entry_key.zfill(4)

            # Insert into dictionary
            dictionary[last_entry_key] = combined_word

            # Add all used dict entries into a list and get their binary codes afterwards
            base_2_value = get_key(latest_char, dictionary)
            compressed += base_2_value

            # Set latest char to the current char after it has been used
            # Always take the second latter to "shift"
            latest_char = current_char
        else:
            latest_char = combined_word

        iteration += 1
        if iteration >= raw_length:
            # At the end, append current character and finish algorithm
            compressed += get_key(current_char, dictionary)
            break

    return compressed, dictionary


# Helper method due to laziness, I want to find values by key in dictionaries
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


main()
