import re
import sample20

lines = sample20.f('イギリス').split('\n')

for i in lines:
    file_line = re.search('(File|ファイル):(.*?)\|', i)
    if file_line is not None:
        #print(file_line)
        print(file_line.group(2))