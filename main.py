from bs4 import BeautifulSoup
import requests

website = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
webpage_html = requests.get(website).text

soup = BeautifulSoup(webpage_html, "html.parser")
titles = [tag.find('a').get_text()for tag in soup.find_all('h3', class_="lister-item-header")]

with open('top_100_movies.txt', 'w') as file:
    file.write("Top 50 Movies on IMDB\n\n")
    for title in titles:
        file.write(f"{titles.index(title) + 1}. {title}\n")