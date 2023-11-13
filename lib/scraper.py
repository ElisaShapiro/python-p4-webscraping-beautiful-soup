# from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# print(doc.select('.heading-primary'))
courses = doc.select('.heading-25-extrabold.color-black')

for course in courses: 
    print(course.contents[0].strip())

# name = doc.select('.heading-60-black.color-black.mb-20')[0].name
name = doc.select('.heading-25-extrabold.color-black')[0].name
print(name)