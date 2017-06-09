from sample40 import Morph

class Chunk:
    def __init__(self, morphs: list, dst: str, srcs: str):
        self.morphs = morphs
        self.dst = int(dst.strip("D"))
        self.srcs = int(srcs)

    def join_morphs(self):
        return ''.join([_morph.surface for _morph in self.morphs if _morph.pos != '記号'])

    def has_noun(self):
        return any([_morph.pos == '名詞' for _morph in self.morphs])

    def has_verb(self):
        return any([_morph.pos == '動詞' for _morph in self.morphs])

    def has_particle(self):
        return any([_morph.pos == '助詞' for _morph in self.morphs])

    def has_sahen_connection_noun_plus_wo(self):
        """
        「サ変接続名詞+を（助詞）」を含むかどうかを返す.
        """
        for idx, _morph in enumerate(self.morphs):
            if _morph.pos == '名詞' and _morph.pos1 == 'サ変接続' and len(self.morphs[idx:]) > 1 and \
                            self.morphs[idx + 1].pos == '助詞' and self.morphs[idx + 1].base == 'を':
                return True

        return False

    def first_verb(self):
        return [_morph for _morph in self.morphs if _morph.pos == '動詞'][0]

    def last_particle(self):
        return [_morph for _morph in self.morphs if _morph.pos == '助詞'][-1]

    def pair(self, sentence: list):
        return self.join_morphs() + '\t' + sentence[self.dst].join_morphs()

    def replace_noun(self, alt: str):
        for _morph in self.morphs:
            if _morph.pos == '名詞':
                _morph.surface = alt

    def __str__(self):
        return 'srcs: {}, dst: {}, morphs: ({})'\
            .format(self.srcs, self.dst, ' / '.join([str(_morph) for _morph in self.morphs]))


def list(text_name):
    sentences = []
    sentence = []
    chunk = None

    with open(text_name) as f:
        for line in f:
            line_list = line.split()

            if line_list[0] == '*':
                if chunk is not None:
                    sentence.append(chunk)
                chunk = Chunk(morphs=[], dst=line_list[2], srcs=line_list[1])

            elif line_list[0] == 'EOS':
                if chunk is not None:
                    sentence.append(chunk)
                if len(sentence) > 0:
                    sentences.append(sentence)
                chunk = None
                sentence = []

            else:
                line_list[1] = line_list[1].replace('*', '')
                line_list = line_list[0].split(',') + line_list[1].split(',')
                morph = Morph(surface=line_list[0], base=line_list[7], pos=line_list[1], pos1=line_list[2])
                chunk.morphs.append(morph)

    return sentences

if __name__ == '__main__':
    chunkeds = list('neko.txt.cabocha')
    for chunk in chunkeds[7]:
        print(chunk)
