import re
from collections import Counter
import math

def clean (myfile):
    newname = '_' + myfile
    out = open(newname, 'w')
    for i,line in enumerate(open(myfile)):
        parts = line.split()
        for x in parts:
            if (re.search('http.*://', x)):
                pass
            else:
                toprint = re.sub('[^a-zA-Z0-9_]','',x)
                toprint = toprint.lower()
                match = 0
                for j,word in enumerate(open('stopwords.txt')):
                    if toprint == word.strip():
                        match = 1
                if match == 0:
                    toprint = (toprint + ' ')
                    out.write(toprint)
    out.close()
    return newname       

def stem (myfile):
    newname = 'preproc' + myfile
    out = open(newname, 'w')
    for i,line in enumerate(open(myfile)):
        parts = line.split()
        for x in parts:
            x = x.strip()
            if (re.search('ly$', x)):
                x = re.sub('ly$','',x)
            if (re.search('ing$', x)):
                x = re.sub('ing$','',x)
            if (re.search('ment$', x)):
                x = re.sub('ment$','',x)
            toprint = x + ' '
            out.write(toprint)
    out.close()
    return newname       

def tf (myfile):
    words = []
    numwords = 0
    for i,line in enumerate(open(myfile)):
        parts = line.split()
        for x in parts:
            words.append(x.strip())
            numwords = numwords + 1
    counts = Counter(words)
    tfs = {}
    for y in counts:
        tfs[y] = counts[y] / numwords
    return tfs

def idf (tfs, myfile):
    numdocs = len(tfs)
    idfs = {}
    for x in tfs[myfile]:
        indocs = 0
        for y in tfs:
            if x in tfs[y]:
                indocs = indocs + 1
        idfs[x] = math.log((numdocs/indocs),math.e) + 1
    return idfs

def tdif (tfs, idfs, myfile):
    tdifs = {}
    for x in tfs[myfile]:
        tdifs[x] = round((tfs[myfile][x] * idfs[myfile][x]), 2)
    return tdifs

def top5 (tdifs, myfile):
    top5 = []
    ordered = sorted(tdifs[myfile].items(), key=lambda x:x[1])
    ordered.reverse()
    while len(top5) < 5:
        for x in ordered:
            if x in top5:
                pass
            else:
                ties = []
                tdif = x[1]
                for y in ordered:
                    if y[1] == tdif:
                        ties.append(y)
                ties = sorted(ties, key=lambda x:x[0])
                for z in ties:
                    if len(top5) < 5:
                        top5.append(z)
    newname = 'tfidf_' + myfile
    #toprint = '[('+top5[0][0]+', '+str(top5[0][1])+'), ('+top5[1][0]+', '+str(top5[1][1])+'), ('+top5[2][0]+', '+str(top5[2][1])+'), ('+top5[3][0]+', '+str(top5[3][1])+'), ('+top5[4][0]+', '+str(top5[4][1])+')]'
    toprint = '['
    for a in top5:
        toprint = toprint + '(' + a[0] + ', ' + str(a[1]) + '), '
    toprint = toprint[:len(toprint)-2]
    toprint = toprint + ']'
    out = open(newname, 'w')
    out.write(toprint)
    out.close()

def main():

    files = []
    for i,line in enumerate(open('tfidf_docs.txt')):
        files.append(line.strip())
    pre = []
    for x in files:
        new = clean(x)
        new = stem(new)
        pre.append(new)
    tfs = {}
    for y in range(len(pre)):
        tfs[files[y]] = tf(pre[y])
    idfs = {}
    for z in files:
        idfs[z] = idf(tfs, z)
    tdifs = {}
    for a in files:
        tdifs[a] = tdif(tfs, idfs, a)
    for b in files:
        top5(tdifs, b)

if __name__=="__main__": 
    main()
