# re means Regular Expressions.
import re

text = "The quick brown fox"
pattern = r"brown" # It will filter the entire text based on given pattern/word in pattern.

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
