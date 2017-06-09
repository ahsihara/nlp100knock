import re  # 正規表現で置き換え
from stemming.porter2 import stem


with open('nlp.txt') as NLP:
    for line in NLP:
        for item in re.sub(r"(?P<group1>[.;:?!])(\s+)(?P<group3>[A-Z])", r"\1\2\n\3", line).split(" "):
            item = re.sub(r"\n", "", item)

            if re.search("\.", item) != None:  # 渡した文字列の中からマッチする部分を探して、そのマッチ部分に対して処理を行うのは、search関数
                print(item + "\t" + stem(item) + "\n")
            else:
                print(item + "\t" + stem(item))
