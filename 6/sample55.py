from pprint import pprint
import json
import corenlp

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)
with open('easy_text.txt', encoding='utf-8') as NLP:
    count = 0
    for line in NLP:
        # XMLで取り出すことは諦めた
        if line != "\n": # 改行記号が単独でparserに入らないようにする
            print(line)
            pprint(parser.raw_parse(line))
            print('----')
            #print(line)
            #print(pasrer.raw_parse(line)["sentences"][0]["words"])
            #for i in parser.raw_parse(line)["sentences"][0]["words"]:
                #print(i[0] + "\t" + str(i[1]["Lemma"]) + "\t" + i[1]["PartOfSpeech"])

        count += 1
        if count > 3: break # とりあえずはじめの方だけ出力