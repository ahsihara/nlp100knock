import re
import sample20

lines = sample20.f('イギリス').split('\n')

for i in lines:
    section_line = re.search('=(=*)\s*(.*?)\s*(=+)$', i)

    if section_line is not None:
        #print(section_line.group(1))
        #print(section_line)
        #print(section_line.group(0))
        print(section_line.group(2), len(section_line.group(1)))


