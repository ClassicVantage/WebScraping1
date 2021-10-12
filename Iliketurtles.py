
from selenium import webdriver
frob bs4 import BeautifulSoup
import time
import csv
import requests

isbrowser=webdriver.Chrome("./chromedriver")

data=[]
starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers=["name", "Distance", "mass", "radius"]