"""wcount.py: count words from an Internet file.

__author__ = "Zhangsan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    def countLetters(text):
        counts = {}
        for l in text:
            counts[l] = counts.get(l,0) + 1
        return counts
    s=lines
    r=s.lower()
    t=r.split()
    u=[]
    for a in t:
        b=[]
        for j in a:
            if (ord(j)>=65 and ord(j)<=90) or (ord(j)>=97 and ord(j)<=122):
                b.append(j)
                c=''.join(b)
        u.append(c)
    v=countLetters(u) 
    w=sorted(v.items(), key=lambda x:x[1], reverse=True)
    y=w[:10]
    print(y)


    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
