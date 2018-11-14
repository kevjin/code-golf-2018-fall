def diff(n1,n2):
    leng = min(len(n1),len(n2))
    for i in range(leng):
        if n1[i]==n2[i]:
            return True
    return False
word = (raw_input()).rstrip()
names = []
cache = {}
while word.isalpha():
    cache[word] = 0
    names.append(word)
    word = (raw_input()).rstrip()
k = word
for n in names:
    for name in names:
        if diff(n,name):
            cache[n]+=1
for key in cache:
    cache[key] = str(cache[key])+key
print(sorted(cache, key=cache.get)[:int(k)])