def domain_name(x):
    """"""



    y = []
    if '//' in x:
        x.split('//')
        x.split('.')
        for i in (x):
            y.append(i)
            return y
        else:
            x.split('.')
            # y.append(i)
    return y


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
print(domain_name("https://www.asos.com"))
print(domain_name("http://www.lenovo.com"))
