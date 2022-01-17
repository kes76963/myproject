import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

movie_url = 'https://movie.naver.com'
# url = f"https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2016&page={i}"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

df = pd.read_csv('./crawling/reviews_2016_.csv')
df.info()


#url 코드 구하기


# url_list = []
# for i in range(1,60):
#    url = f"https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2016&page={i}"
#    req = requests.get(url)
#    soup = BeautifulSoup(req.text, "html.parser")
#
#    for href in soup.find("ul", class_="directory_list").find_all("li"):
#       list = href.find("a")["href"]
#       if 'code' in list :
#          url_list.append(list)
#    print(i,'페이지 완료')
# print(url_list)



url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=144773#"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print("The href links are :")

list2 = []
for href in soup.find("ul", class_="rvw_list_area").find_all("li"):
   #list = href.find("a").split('showReviewDetail')
   list = href.find("a")
   list = re.findall('\(([^)]+)',str(list))[1]
   print(list)
   #list = re.findall('\((.*)\)',list)
   #list2.append(list)
   # list2 = re.findall('\(([^)]+)',list)
   # print(list2)

#print(list2)
#
# list3 = re.findall('\(([^)]+)',list2[1])
# print(list3)
# pattern = re.compile(r'([0-9]+)[^-]')  # find number groups after `-` character
# result = re.findall(pattern, list2[1])
# print(result)

