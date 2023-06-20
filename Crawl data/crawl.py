import requests
from bs4 import BeautifulSoup
import pyodbc

SERVER_NAME= 'DESKTOP-IKUJLM5'
DRIVER_NAME='SQL SERVER'
DATABASE_NAME='crawl'
connection_str=f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
con=pyodbc.connect(connection_str)
print(con)
cursor=con.cursor()


url = "https://www.trustpilot.com/review/litextension.com"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

tag = soup.find_all('div', {'class': 'styles_reviewCardInner__EwDq2'})

for i in tag:
    print('Name of customer: ')
    name = i.find('span', {'class': 'typography_heading-xxs__QKBS8 typography_appearance-default__AAY17'}).text
    print(name)
    country = i.find('div', {
        'class': 'typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_detailsIcon__Fo_ua'})
    country1 = country.find('span').text
    print(country1)

    rate = i.find('div', {'class': 'styles_reviewHeader__iU9Px'})

    print(rate)

    print('Title is: ')
    title = i.find('h2', {'class': 'typography_heading-s__f7029 typography_appearance-default__AAY17'}).text
    print(title)

    print('Content is: ')
    content = i.find('p', {
        'class': 'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'}).text.splitlines()[:2]
    print(content)

    date_of_experience = i.find('p', {
        'class': 'typography_body-m__xgxZ_ typography_appearance-default__AAY17'}).text.split()[3:]
    print(date_of_experience[0]+'/'+date_of_experience[1].replace(',','')+'/'+date_of_experience[2])
    print('----------------')
    sql = ("INSERT INTO dataCrawl(  CustomerName, Title, Content, Rate, Country, DateOfExperience) VALUES(?,?,?,?,?,?)")
    Values=[name,title,content,rate,country1,date_of_experience]
    print(Values)
    print("Insert ")
    # cursor.execute(sql,Values).commit()




