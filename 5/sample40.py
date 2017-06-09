class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def end_of_sentence(self):
        if self.pos1 == '句点':
            return 1
        else:
            return 0

    def __str__(self):
        return 'surface: {}, base: {}, pos: {}, pos1: {}'\
            .format(self.surface, self.base, self.pos, self.pos1)


def list(text_name):
    sentences = []
    sentence = []
    with open(text_name) as f:
        for line in f:
            lis = line.split()
            if lis[0] != '*' and lis[0] != 'EOS':
                lis[1] = lis[1].replace('*', '')
                lis2 = lis[0].split(',') + lis[1].split(',')
                morph = Morph(surface=lis2[0], base=lis2[7], pos=lis2[1], pos1=lis2[2])

                sentence.append(morph)

                #句点で区切る
                if morph.end_of_sentence():
                    sentences.append(sentence)
                    sentence = []

    return sentences

if __name__ == '__main__':
    sentences = list('neko.txt.cabocha')
    for morph in sentences[2]:
        print(morph)