from bs4 import BeautifulSoup
import lxml
import requests
#
# with open("website.html", "r") as file:
#     file_data = file.read()
#
# soup = BeautifulSoup(file_data, "html.parser")
# print(soup.prettify())  # nicely formatted
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)  # find the first a tag
#
# # get all specified tags
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# # get a specific element by tag and id or class
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.get("class"))
#
#
# # find objects using css selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# heading_2 = soup.select_one(selector="#name")
# headings = soup.select(selector=".heading")


# Info from live website
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
# print(yc_web_page)
soup = BeautifulSoup(yc_web_page, "html.parser")

## Get all titles and article links
# all_rows = soup.find_all(name="tr", class_="athing")
#
# for row in all_rows:
#     pass
#     article_info = row.select_one(selector=".titleline")
#     article_title = article_info.text
#     article_link = article_info.select_one(selector="a").get("href")
#     print(article_link)

## Get all scores and find the hightest
all_scores = soup.find_all(name="span", class_="score")

# max_score = 0
# max_score_obj = 0
# for score in all_scores:
#     score_value = int(score.text.split(" ")[0])
#     if score_value > max_score:
#         max_score_obj = score
#         max_score = score_value
#
# print(max_score)
# print(max_score_obj)

max_score_obj = max(all_scores, key=lambda val: int(val.text.split(" ")[0]))
# print(max_score_obj)
max_score_id = max_score_obj.get("id").split("_")[1]
# print(max_score_id)

title_span = soup.find(class_="athing", id=str(max_score_id)).find(class_="titleline")

out_ = f"Title: {title_span.text} \n" \
       f"Link: {title_span.find(name='a').get('href')}"
print(out_)

## robots.txt to see what is allowed or not, delay for crawling


