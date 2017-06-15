import corenlp

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

def kadai50():

    a = 'nlp.txt'

    kadai = []
    with open(a) as f:
        sentences = f.read()
        sentence = sentences.split('.\n\n')
        for i in range(len(sentence)):
            check = parser.raw_parse(sentence[i])
            for j in range(len(check['sentences'])):
                kadai.append(check['sentences'][j]['text'])

        print(len(kadai))

    return kadai

if __name__ == '__main__':
    kadai = kadai50()
    for i in range(len(kadai)):
        print(kadai[i])
        print()

