url ='file3.txt'
with open(url,'r') as f:
    x = f.readlines()
    for sens in x:
        words = sens.split()
        for word in words:
            for c in word:
                print(ord(c.lower())-96)