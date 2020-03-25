import os
import nltk

documents = "/home/min/Documents/school/is392/assignments/hw2/pages"

def indexer(documents):
    #make hashtable
    posIndex = {}
    countIndex = {}
    n = 0 #doc number
    for filename in os.listdir(documents):
        if filename.endswith(".txt"):
            n += 1
            f = open(documents+"/"+filename)
            text = f.read()
            tokens = nltk.word_tokenize(text)
            tokCount = 0
            docIndex = {}
            for token in tokens:
                #print(token)
                #token counts per document
                tokCount += 1
                if token not in docIndex:
                    docIndex[token] = 1
                else:
                    docIndex[token] += 1
                if token not in posIndex:
                    posIndex[token] = []
                    posIndex[token].append((n,tokCount)) #this is for indexer position
                else:
                    posIndex[token].append((n,tokCount)) 
                #print(key)
            #print(lines)
            print("doc # = %d" % (n))
            #if n>=5:
            #    break
            for token in docIndex:
                if token not in countIndex:
                    countIndex[token] = []
                    countIndex[token].append((n, docIndex[token]))
                else:
                    countIndex[token].append((n, docIndex[token]))
                continue
        else:
            print("not a valid .txt")
            continue
    f = open('posIndex.txt', 'w', encoding = 'utf-8')
    for term in posIndex:
        f.write(term+' => ')
        for posting in posIndex[term]:
            f.write('(%d, %d) ' % (posting[0], posting[1]))
        f.write('\n')
    f.close()
    
    s = open('freqIndex.txt', 'w', encoding = 'utf-8')
    for term in countIndex:
        s.write(term+' => ')
        for posting in countIndex[term]:
            s.write('(%d, %d) ' % (posting[0], posting[1]))
        s.write('\n')
    s.close()

indexer(documents)
