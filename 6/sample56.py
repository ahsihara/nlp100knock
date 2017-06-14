import re
from xml.etree import ElementTree
from sample51 import make_word_list

tree = ElementTree.parse("nlp.txt.xml") # ElementTreeでパーシング
root = tree.getroot()

def make_src():
    src = []
    #global sentences
    sentences = []
    for sentence in root[0][0]:
        for token in sentence[0]:
            sentences.append(token[0].text)
        src.append(sentences)
        sentences = []

    return src

def make_coreference():
    coreferences ,mentions = [], []
    tags = {}
    for coreference in root[0][1]:
        for mention in coreference:
            b = mention.attrib
            if b.keys():
                tags["representative"]=b['representative']
            for m in mention:
                tags[m.tag]=m.text
            mentions.append(tags)
            tags = {}
        coreferences.append(mentions)
        mentions = []
    return coreferences

def make_referenceslist():
    referenceslist = []
    for coreferencex in coreferences:
        for mentionx in coreferencex:
            if "representative" in mentionx:
                #print(mentionx)
                #representative_text = mentionx["text"]
                aa, bb, cc = int(mentionx['sentence'])-1, int(mentionx['start'])-1, int(mentionx['end'])-1
                #aa = mentionx['sentence']
                #print(aa, bb, cc)
                try:
                    representative_text = ' '.join(word_list[aa][bb:cc])
                except:
                    representative_text = 'wwwww'
                #representative_text = 'aaa'
                representative_text = re.sub(r'-LRB- ',r'(',representative_text)
                representative_text = re.sub(r' -RRB-',r')',representative_text)
                representative_text = "「"+representative_text+"("
            else:
                referenceslist.append([mentionx["sentence"],mentionx["start"],representative_text])
                referenceslist.append([mentionx["sentence"],mentionx["end"],")」"])
    return referenceslist

def print_ans():
    tokens = []
    n = 1
    m = 1
    for sentence in src:
        for tokens in sentence:
            for x in referenceslist:
                if int(x[0]) == n and int(x[1]) == m:
                    print(x[2], end="")
            tokens = re.sub(r'-LRB-', r'(', tokens)
            tokens = re.sub(r'-RRB-', r')', tokens)
            print(tokens, end=" ")
            m += 1
        print("")
        m = 1
        n += 1

if __name__ == "__main__":
    word_list = make_word_list()
    src = make_src()
    coreferences = make_coreference()
    referenceslist = make_referenceslist()
    print_ans()