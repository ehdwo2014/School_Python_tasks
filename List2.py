import nltk
import string


print("Please select Task Number")
TaskNumber  = int(input())
print(TaskNumber)

if TaskNumber == 12:
    print("input d = ")
    d = input()
    print("text = ")
    t = input()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    Buf = ""
    for i in range (int(d), len(alpha)):
        Buf = Buf+alpha[i]
    for i in range(0, int(d)):
        Buf = Buf+alpha[i]
    table = str.maketrans(alpha, Buf)
    print(t.translate(table))

if TaskNumber == 13:
    print("Input Sub-task")
    n = input()
    if(n == 'a'):
        f = open('C:\\Users\DongJae Yoon\Desktop\Python\Catch22.txt', 'rt', encoding='UTF8')
        f1 = open('C:\\Users\DongJae Yoon\Desktop\Python\Catch22_mod1.txt', 'w', encoding='UTF8')
        print(string.punctuation)
        table = str.maketrans('', '',string.punctuation)
        while True:
            line = f.readline().translate(table)
            f1.write(line)
            if not line: break
            print(line)
        f.close()
        f1.close()

    if(n == 'b'):
        from nltk.corpus import stopwords
        from stop_words import get_stop_words

        stop_words = list(get_stop_words('en'))  # About 900 stopwords
        nltk_words = list(stopwords.words('english'))  # About 150 stopwords
        stop_words.extend(nltk_words)
        STOPWORDS = set(stopwords.words('english'))
        f = open('C:\\Users\DongJae Yoon\Desktop\Python\Catch22.txt', 'rt', encoding='UTF8')
        f1 = open('C:\\Users\DongJae Yoon\Desktop\Python\Catch22_mod2.txt', 'w', encoding='UTF8')
        line = f.read()
        line = ' '.join([word for word in line.split() if word.lower() not in STOPWORDS])  # delete stopwords from text
        f1.write(line)
        print(STOPWORDS)

        f.close()
        f1.close()

    if (n == 'c'):
        from nltk.stem import PorterStemmer
        from nltk.tokenize import word_tokenize
        s = PorterStemmer()
        f = open('C:\\Users\DongJae Yoon\Desktop\Python\Catch22_mod.txt', 'rt', encoding='UTF8')
        f1 = open('C:\\Users\DongJae Yoon\Desktop\Python\Catch22_mod3.txt', 'w', encoding='UTF8')
        text = f.read()
        words=word_tokenize(text)
        text = ' '.join([word for word in text.split() if word.lower() in words])
        f1.write(text)
        f.close()
        f1.close()

    if(n == 'd'):
        from collections import Counter
        from nltk.tokenize import word_tokenize
        f = open('C:\\Users\DongJae Yoon\Desktop\Python\Catch22_mod.txt', 'rt', encoding='UTF8')
        text = f.read()
        words=word_tokenize(text)
        sw = ['.', ',']
        removed_list = []
        for word in words:
            if word.lower() not in sw:
                removed_list.append(word.lower())
        count_list = Counter(removed_list)
        common_cl = count_list.most_common()
        print(common_cl)

        v = []

        for k in count_list.keys():
            if(int(count_list.get(k)) > 100 ):
                v.append(k)

        v.sort()
        print("Sorted words list where f > 100 in alphabetical order ")
        print(v)

if TaskNumber == 14:
    DN = {'Denis': 'Wielka 22', 'Yooni': 'PlacZgody 5', 'Paula': 'Jableczna 28', 'Mateusz': 'Gaj 21'}
    sortedDN = sorted(DN.items(), key=lambda x: x[1], reverse=False)
    print(sortedDN)

if TaskNumber == 15:
    from nltk.book import *
    print("word frequency of 'knight' in text6: ")
    print(text6.count('knight'))
    print("word frequency of 'knight' in text7: ")
    print(text7.count('knight'))

if TaskNumber == 16:
    from nltk.book import *
    a = set(text6) - set(text7)
    print(a)

if TaskNumber == 17:
    from nltk.book import *
    a = set.union(set(text1), set(text2), set(text3), set(text4), set(text5), set(text6), set(text7), set(text8), set(text9))
    print(a)
    print(len(a))

if TaskNumber == 18:
    from nltk.book import *
    from nltk.tokenize import sent_tokenize
    f = open('C:\\Users\DongJae Yoon\AppData\Roaming\\nltk_data\corpora\gutenberg\\austen-sense.txt', 'rt', encoding='UTF8')
    st = sent_tokenize(f.read())
    word_count = lambda st: len(st)
    print(max(st, key=word_count))  # the longest sentence by word count

    f.close()

if TaskNumber == 19:
    import random
    from nltk.book import *
    L = random.randint(1, 6)
    q = []
    print("L is :")
    print(L)
    for w in set(text6):
        if len(w) == L:
            q.append(w)
    print(q)