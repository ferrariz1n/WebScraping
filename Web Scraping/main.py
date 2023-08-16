#Bibliotecas
import requests
from bs4 import BeautifulSoup
import csv

link = "https://www.reddit.com/r/programming/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

requisicao = requests.get(link, headers=headers)
site=BeautifulSoup(requisicao.text, "html.parser")
posts=site.find_all('shreddit-post', {'view-context':'SubredditFeed'})
titles=[]
upvotes=[]
links=[]


for i in range(3):
    post=posts[i]
    #titulo
    title= post.find('div', {'slot':'title'})
    titles.append(title.text)
    #Votos
    upvote_value=posts[i]['score']
    upvotes.append(upvote_value)
    #Link
    link= post.find('a',{'class':'absolute inset-0'})
    href_value = link['href']
    links.append(href_value)
   


#Salvar CSV
with open("webscraping.csv", 'w', newline='') as csvfile:
    campos_head = ['Nome', 'UpVotes', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=campos_head)
    
    writer.writeheader()
    writer.writerow({'Nome':'{titles}','UpVotes':'{upvotes}', 'Link':'{links}'})
    
    for i in range(len(titles)):
        writer.writerow({'Nome': titles[i], 'UpVotes': upvotes[i], 'Link': links[i]})