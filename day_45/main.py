# --To scrap a local html file, in this case, website.html
# Import the BeautifulSoup library
from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# --Gets the tag and the content of the tag
# print(soup.title)

# -- Gets only the name of the tag
# print(soup.title.name)

# --Gets the content of the tag
# print(soup.title.string)

# --Gets all the content of the html with its indentation
# print(soup.prettify())

# -- Gets the first type of tag of the html
# print(soup.find(name="p")
# print(soup.p)

# --Finds all the tags of the specified type
all_p_tags = soup.findAll(name="p")
all_a_tags = soup.findAll(name="a")

# for tag in all_p_tags:
#     print(tag.getText())
#
# for tag in all_a_tags:
#     print(tag.get("href"))

heading = soup.findAll(name="h1", id="name")
print(heading)

# Notice that if you just put "class" in the param, you will get an error because
# it is a reserved word in python, to solve it add an "_", -->  class_
section_heading = soup.findAll(name="h3", class_="heading")

# use css selectors to find a particular element

company_url = soup.select_one(selector="p a")
print(company_url)
