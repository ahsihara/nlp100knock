
import re
import sample20


def remove_markup(str):
    str = re.sub("'+", '', str)
    str = re.sub('\[{2}([^|\]]+?\|)*(.+?)\]{2}', r'\2', str)
    return str

temp_dict = {}
lines = sample20.f('イギリス').split('\n')

for i in lines:
    category_line = re.search('^\|(.*?)\s=\s(.*)', i)
    if category_line is not None:
        temp_dict[category_line.group(1)] = remove_markup(category_line.group(2))

for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
    print(k, v)