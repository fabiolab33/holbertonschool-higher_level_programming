#!/usr/bin/python3
# Print the loweercase ASCII alphabet, skipping 'q' and 'e', no newline at the end

for c in range(97, 123):
    if chr(c) not in ('q', 'e'):
        print("{}".format(chr(c)), end="")
