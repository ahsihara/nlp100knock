import sample41

def sorted_double_list(key_list, value_list):
    double_list = list(zip(key_list, value_list))
    double_list = dict(double_list)
    double_list = sorted(double_list.items())
    return [pair[0] for pair in double_list], [pair[1] for pair in double_list]

def case_frame_patterns(_chunked_sentences):
    _case_frame_patterns = []
    for sentence in _chunked_sentences:
        for _chunk in sentence:
            if _chunk.has_verb():
                clauses = [c.join_morphs() for c in sentence if c.dst == _chunk.srcs and c.has_particle()]
                #print(_chunk.srcs)
                particles = [c.last_particle().base for c in sentence if c.dst == _chunk.srcs and c.has_particle()]

                if len(particles) > 0:
                    _case_frame_patterns.append([_chunk.first_verb().base, *sorted_double_list(particles, clauses)])

    return _case_frame_patterns

def print_ans(_case_frame_patterns):
    ans = []
    for case in _case_frame_patterns:
        ans.append(case[0] + '\t' +' '.join(case[1]) + '\t' + ' '.join(case[2]))

    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    chunkeds = sample41.list('neko.txt.cabocha')
    print_ans(case_frame_patterns(chunkeds))
