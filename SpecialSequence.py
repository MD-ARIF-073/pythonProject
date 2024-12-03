import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print ("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print ("Match 3")




import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")



import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
    print ("Match 3")

match = re.search(pattern, "We/cat.tered.")
if match:
    print ("Match 4")

match = re.search(pattern, "We{cat!tered.")
if match:
    print ("Match 5")