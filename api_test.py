
import requests
import  json
from pprint import pprint

def news_api():
    asskey="1d23bcfffc9f2ab1ec0f4265a3e782a3"
    ip='154.68.197.50'
    url = 'https://newsapi.org/v2/top-headlines?q=tesla&from=2021-12-16&sortBy=publishedAt&apiKey=7592c6a9adcf478ab80bd16bacb6e0ac'

    r=requests.get(url)

    # r=requests.get(url, params=body)
    text=r.text
    j=r.json()
    status=r.status_code
    article = j["articles"]
    results = []

    # for ar in article:
    #     results.append(ar["title"])
    #     results.append(ar["author"])
    #     results.append(ar["description"])
            
    # for i in range(len(results)):
            
    #     # printing all trending news
    #     print(i + 1, results[i])

    # print(json.dumps(j['articles'], indent=2))
    for i in j['articles']:
        # print(json.dumps(i['source']['id'], indent=2))
        # print()
        author=i['author']
        title=i['title']
        desc=i['description']
        words=i['title']
        author=f'Author: {author}'
        title=f'title: {title}'
        desc=f'desc: {desc}'
        # arr = words.split()
        print(author)
        print(title)
        print(desc)
        print("!!!!!")
    return author, title, desc
# news_api()


url = 'https://newsapi.org/v2/top-headlines?q=tesla&from=2021-12-16&sortBy=publishedAt&apiKey=7592c6a9adcf478ab80bd16bacb6e0ac'
r=requests.get(url)

j=r.json()
article = j["articles"]


