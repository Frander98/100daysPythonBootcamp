# Import the BeautifulSoup library and colorama
from colorama import Fore, init
from bs4 import BeautifulSoup
import requests

init()
yc_tech_news = requests.get("https://news.ycombinator.com/").text

soup = BeautifulSoup(yc_tech_news, "html.parser")
news_titles_tag = soup.findAll(name="a", class_="titlelink")
news_votes_tags = soup.findAll(name="span", class_="score")
news_text = []
news_links = []
news_votes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]


for title in news_titles_tag:
    news_text.append(title.getText())
    news_links.append(title.get("href"))

# print(news_text)
# print(news_links)
# print(news_votes)

# Get the title and the link of the most votes article
most_voted_article_index = news_votes.index(max(news_votes))
print(Fore.MAGENTA + f"Title: {news_text[most_voted_article_index]}.\n{Fore.YELLOW}Link: {news_links[most_voted_article_index]}{Fore.CYAN}\nVotes: {max(news_votes)}")




