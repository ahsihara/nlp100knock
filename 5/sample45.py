from sample41 import list
import subprocess
from pprint import pprint

def case_patterns(_chunked_sentences):
    _case_pattern = []
    for sentence in _chunked_sentences:
        for _chunk in sentence:
            if not _chunk.has_verb():
                continue

            particles = [c.last_particle().base for c in sentence if c.dst == _chunk.srcs and c.has_particle()]

            if len(particles) > 0:
                _case_pattern.append([_chunk.first_verb().base, sorted(particles)])

    return _case_pattern


def print_ans(_case_patterns):
    ans = []
    for _case in _case_patterns:
        ans.append(_case[0] + '\t' + ' '.join(_case[1]))
    for i in range(10):
        print(ans[i])



def print_case_pattern_ranking(_grep_str):
    _grep_str = '' if _grep_str == '' else '| grep \'^{}\t\''.format(_grep_str)
    print(subprocess.run('cat case_patterns.txt {} | sort | uniq -c | sort -r | head -10'.format(_grep_str), shell=True))


if __name__ == '__main__':
    chunkeds = list('neko.txt.cabocha')
    print_ans(case_patterns(chunkeds))