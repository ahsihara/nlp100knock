
import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
coreference = root.findall('document/sentences/sentence/dependencies[@type="collapsed-dependencies"]')

def search_verb(co_dependence):
    verb_nsubj = []
    verb_dobj = []
    nsubj = []#[親番号、自分の文字]
    dobj = []#[親番号、自分の文字]

    nsubj_line = co_dependence.findall('dep[@type="nsubj"]')
    dobj_line = co_dependence.findall('dep[@type="dobj"]')

    for i in nsubj_line:
        governor = i.find('governor')
        dependent = i.find('dependent')
        verb_nsubj.append((governor.get('idx'), governor.text))
        nsubj.append((governor.get('idx'), dependent.text))
    for i in dobj_line:
        governor = i.find('governor')
        dependent = i.find('dependent')
        verb_dobj.append((governor.get('idx'), governor.text))
        dobj.append((governor.get('idx'), dependent.text))

    verb = list(set(verb_nsubj) & set(verb_dobj))

    return verb, nsubj, dobj

def print_ans(verb, nsubj, dobj):
    for i in verb:
        flg_nsubj, flg_dobj = 0, 0
        idx = i[0]

        for j in nsubj:
            if j[0] == idx:
                flg_nsubj = j
                break
        for j in dobj:
            if j[0] == idx:
                flg_dobj = j
                break

        if flg_nsubj != 0 and flg_dobj != 0:
            print('{}\t{}\t{}'.format(flg_nsubj[1], i[1], flg_dobj[1]))

def make_taple(co_dependence):
    verb, nsubj, dobj = search_verb(co_dependence)
    if len(verb) == 0:
        return
    print_ans(verb, nsubj, dobj)


if __name__ == '__main__':
    for i in range(len(coreference)):
        make_taple(coreference[i])
