text = 'I am an NLPer'
text2 = text.split()

def ngram(text, n):
    for i in range(len(text) - n + 1):
        for j in range(n):
            print(text[i+j],end = ' ')
        print('')

ngram(text2, 2)
ngram(text, 2)
