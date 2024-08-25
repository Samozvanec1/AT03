import  requests
import os

def get_cat():
    url = 'https://api.thecatapi.com/v1/images/search'
    zanpoc = requests.get(url)
    if zanpoc.status_code == 200:
        per = zanpoc.json()[0]['url'] # json - это словарь или список
        per = requests.get(per).content
        return per
    else:
        return None




if __name__ == '__main__':
    count = 1
    if not os.path.exists("counting_cats.txt"):
        with open("counting_cats.txt", "w") as o:
            pass
    with open("counting_cats.txt", "r") as f:
        counts_here = f.read()
        if not counts_here == '':
            count = int(counts_here)
    with open("counting_cats.txt", "w") as o:
        o.write(str(count + 1))
    with open(f"cat{count}.jpg", "wb") as g:
        g.write(get_cat())