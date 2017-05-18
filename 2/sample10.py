
if __name__ == '__main__':
    with open('hightemp.txt') as f:
        lines = f.readlines()
        print(len(lines))

'''
import codecs
codecs.open('.txt', 'r', 'utf-8')
'''