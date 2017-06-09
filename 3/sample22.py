import re
import sample20

lines = sample20.f('イギリス').split('\n')

for i in lines:
    category_line = re.search('^\[\[Category:(.*?)(\|\*)?\]\]', i)
    if category_line is not None:

        #print(i)
        #print(category_line)
        #print(category_line.group())
        print(category_line.group(1))
        '''
        i2 = i.replace('[[Category:', '')
        i3 = i2.replace(']]', '')
        i4 = i3.replace('|*', '')
        print(i4)
        '''
#<_sre.SRE_Match object; span=(0, 19), match='[[Category:イギリス|*]]'>
