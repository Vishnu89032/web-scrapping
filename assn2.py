import requests
from bs4 import BeautifulSoup


def get_latest_python_article():
    url="https://www.python.org"
    response=requests.get(url)

    if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        latest_article=[]

        for article in soup.select(".event-widget li"):
            title=article.a.text.strip()
            latest_article.append(title)

        return latest_article
    else:
        print(f"fail to retrieve information.status code:{response.status.code}")
        return []
    
if __name__=="__main__":
    python_article=get_latest_python_article()

    if python_article:
        print("New News in the python.org section")
        for index,article in enumerate(python_article,1):
            print(f"{index}.{article}")

    else:
        print("no article found")
        

    