def exchange(currency_from, currency_to, amount_from):
    a=str(currency_from)
    b=str(currency_to)
    c=float(amount_from)
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(a, b, c))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    s=jstr
    t=s.split('"')
    u=t[7]
    v=u.split()
    w=v[0]
    print(w)
    
currency_from=input()
currency_to=input()
amount_from=input()
exchange(currency_from, currency_to, amount_from)
