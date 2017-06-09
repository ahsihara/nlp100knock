import MeCab

def f(input_file_name, output_file_name):
    m = MeCab.Tagger('-Ochasen')
    with open(input_file_name) as g, open(output_file_name, 'w') as h:
        sentence = g.read()
        line = m.parse(sentence)
        h.write(line)

f('neko.txt', 'neko.txt.mecab')