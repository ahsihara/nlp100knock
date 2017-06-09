import json

def f(title):
    with open('jawiki-country.json') as f:
        line = f.readline()
        while line:
            article_dict = json.loads(line)
            #print(article_dict)
            if article_dict['title'] == title:
                return article_dict['text']
                #print(article_dict['text'])
                #return
                #line = f.readline()
            else:
                line = f.readline()
    return ''
if __name__ == '__main__':
    print(f('イギリス'))
    #f('イギリス')