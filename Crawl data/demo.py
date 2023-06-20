from datetime import datetime

import requests
from bs4 import BeautifulSoup
import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='L0367970712@',
    database='crawl'
)
if con.is_connected():
    print("Connect")
cursor = con.cursor()

url = "https://www.trustpilot.com/review/litextension.com?page="
for page in range(1,77):
    r = requests.get(url+str(page))
    soup = BeautifulSoup(r.content, 'html.parser')

    reviews = soup.css.select('.styles_reviewCardInner__EwDq2')

    for i in range(len(reviews)):
        name = reviews[i].select_one('a>span').text
        # print(name)
        rating = reviews[i].select_one('section>div')['data-service-review-rating']
        # print(rating)
        title = reviews[i].select_one('div>a>h2').text
        # print(title)
        content = reviews[i].select_one('div>p').text
        # print(content)
        country = reviews[i].select_one('a>div>div>span').text
        # print(country)
        date_of_experience = reviews[i].find('p', {
            'class': 'typography_body-m__xgxZ_ typography_appearance-default__AAY17'}).text.split()[3:]
        date = date_of_experience[0] + '/' + date_of_experience[1].replace(',', '') + '/' + date_of_experience[2]
        newdate=datetime.strptime(date,'%B/%d/%Y').date().strftime("%Y/%m/%d")
        # print(newdate)
        print('---------------')
        sql = "INSERT INTO dataCrawl(CustomerName, Title, Content, Rate, Country, DateOfExperience) VALUES(%s,%s,%s,%s,%s,%s)"
        Values = [name, title, content, rating, country, newdate]
        # print(Values)
        print("Insert ")

        cursor.execute(sql, Values)
        con.commit()
    print("End "+str(page))


