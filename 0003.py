s = "aabaabcbb"

longest_length = 0
second_longest_length = 0
longest_str = ""
second_longest_str = ""
str_start_index = 0
for i, e in enumerate(s):
    if second_longest_length != 0:
        if e not in second_longest_str:
            second_longest_str += e
            second_longest_length += 1
        else:
            second_longest_length -= len(second_longest_str.split(e)[0])
            second_longest_str = second_longest_str.split(e)[1] + e
        if second_longest_length > longest_length:
            longest_str = second_longest_str
            longest_length = second_longest_length
            second_longest_str = ""
            second_longest_length = 0
    else:
        if e not in longest_str:
            longest_str += e
            longest_length += 1
        else:
            if longest_str[0] != e:
                second_longest_str = longest_str.split(e)[1] + e
                second_longest_length = len(second_longest_str)
            else:
                longest_str = longest_str[1:] + e

print(longest_str)

