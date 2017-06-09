import sample41
import subprocess
from sample46 import sorted_double_list

def sahen_case_frame_patterns(_chunked_sentences):
    _sahen_case_frame_patterns = []
    for sentence in _chunked_sentences:
        for _chunk in sentence:
            if not _chunk.has_verb():
                continue

            sahen_connection_noun = [c.join_morphs() for c in sentence if c.dst == _chunk.srcs and c.has_sahen_connection_noun_plus_wo()]
            clauses = [c.join_morphs() for c in sentence if c.dst == _chunk.srcs and not c.has_sahen_connection_noun_plus_wo() and c.has_particle()]
            particles = [c.last_particle().base for c in sentence if c.dst == _chunk.srcs and not c.has_sahen_connection_noun_plus_wo() and c.has_particle()]

            if len(sahen_connection_noun) > 0 and len(particles) > 0:
                _sahen_case_frame_patterns.append([sahen_connection_noun[0] + _chunk.first_verb().base, *sorted_double_list(particles, clauses)])

    return _sahen_case_frame_patterns


def print_ans(_sahen_case_frame_patterns):
    ans = []
    for case in _sahen_case_frame_patterns:
        ans.append(case[0] + '\t' + ' '.join(case[1]) + '\t' + ' '.join(case[2]))

    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    chunkeds = sample41.list('neko.txt.cabocha')
    print_ans(sahen_case_frame_patterns(chunkeds))

    #print(subprocess.run('cat sahen_case_frame_patterns.txt | cut -f 1 | sort | uniq -c | sort -r | head -10', shell=True))
    #print(subprocess.run('cat sahen_case_frame_patterns.txt | cut -f 1,2 | sort | uniq -c | sort -r | head -10', shell=True))
