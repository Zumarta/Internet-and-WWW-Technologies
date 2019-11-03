# Does the god damn calculation for the homework
import math

def calc_sum(relative_frequencies):
    sum_of_frequencies = 0
    for n in relative_frequencies:
        sum_of_frequencies += n

    return sum_of_frequencies


# Relative Haeufigkeiten von Codes
relative_frequencies = [20, 20, 20, 15, 15, 11, 10, 10, 10, 10, 7, 6, 6, 3, 3, 3, 3, 2]

sum_of_frequencies = calc_sum(relative_frequencies)

entropy = 0
for i in relative_frequencies:
    probability = i / sum_of_frequencies
    entropy += (-probability * math.log2(probability))

print(entropy)
