import corenlp

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

def kadai50():

    a = 'nlp.txt'
    b = '../../study/practice_core/easy_text.txt'
    kadai = []
    with open(a) as f:
        sentences = f.read()
        check = parser.raw_parse(sentences)
        for i in range(len(check['sentences'])):
            kadai.append(check['sentences'][i]['text'])

    return kadai

if __name__ == '__main__':
    kadai = kadai50()
    for i in range(len(kadai)):
        print(kadai[i])
        print('')



