import re
def replace_symbols(text):
    text=re.sub(r"(?<=)&&(?=)","and",text)
    text=re.sub(r"(?<=)\|\|(?=)","or",text)
    return text
n=int(input())
lines=[input() for _ in range(n)]
modified_lines=[replace_symbols(line) for line in lines]
for line in modified_lines:
    print(line)
