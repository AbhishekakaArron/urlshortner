import string
import random
N = 8
baseurl = "https://www.mywebsite.com/"

hashmap = {"asdkajb": "www.poscapsoc.com","ascnlkn":"www.onion.com","abc":"www.hashmaps.com"}
def urlgenerator(url):
    random_check = True
    if url in hashmap:
        print(hashmap[url])
    else:
        while(random_check):
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
            if res in hashmap:
                random_check=True
            else:
                random_check=False
        hashmap[baseurl+res] = url
        return res + ":" + url
        
urlGen = urlgenerator("www.gfg.com")
print(urlGen)
print(hashmap)
