import re
import sample20

temp_dict = {}
lines = re.split('\n[\|}]', sample20.f('イギリス'))

for i in lines:
    temp_line = re.search('^(.*?)\s=\s(.*)', i, re.S)
    if temp_line is not None:
        temp_dict[temp_line.group(1)] = temp_line.group(2)

for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
    print(k, v)
