import sample20
import re

lines = sample20.f('イギリス').split('\n')
'''
for i in lines:
    if 'Category' in i:
        print(i)
'''
for i in lines:
    category_line = re.search('\[\[Category:(.*?)\]\]', i)
    if category_line is not None:

        #print(i)
        #print(category_line)
        print(category_line.group())
#'''