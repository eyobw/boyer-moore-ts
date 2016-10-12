"""
Eyob W.
"""

__author__ = "Eyob W"
__date__ = "Date: 30.1.2015"
__version__ = "Version: 1.0"
__Copyright__ = "Copyright: @eyobw"


input_pattern = 'vulputate'
# Initialize input text
input_text = ''

# Read the text file
with open('sample_text.txt', encoding="utf8") as f:
    input_text = f.read()


# Search function
def boyer_moore_search(text, pattern):
    # initialize counter
    counter = 0

    # All matches will be stored in an array
    matches = []

    match_table = {}
    for y, x in reversed(list(enumerate(pattern))):
        if x in match_table:
            match_table[x].append(y)
        else: match_table[x] = [y]

    shifts = []
    pattern_end = len(pattern) - 1  # the last character in the pattern

    i = j = pattern_end  # i for text j for pattern

    k = i

    while i < len(text):
        # Compare pattern with the text
        if text[i] == pattern[j]:
            if j > 0:
                i -= 1
                j -= 1
            elif j == 0:
                matches.append(i)
                counter += 1  # Increase counter by 1
                if shifts:
                    i = sum(shifts.pop())
                else:
                    i = k + 1

                k = i
                j = pattern_end
        else:
            if text[i] in match_table:
                for match_position in match_table[text[i]]:
                    if match_position < j:
                        shifts.insert(0, (k, pattern_end - match_position))

            if shifts:
                counter += 1
                i = sum(shifts.pop())
            else:
                i = k + pattern_end
            k = i
            j = pattern_end
    result = "%d searches made and matches found at %s" %(counter, matches)
    return result

if __name__ == "__main__":
    print(boyer_moore_search(input_text, input_pattern))
