from bs4 import BeautifulSoup
import re
import requests
import time 

url = "https://www.theyfightcrime.org/"
male_characters = open("Male_Characters.txt","w+")
female_characters = open("Female_Characters.txt", "w+")

for x in range(1,51):
    data = requests.get(url)
    if data.status_code == 200:
        soup = BeautifulSoup(data.content, 'html.parser')
        characters = soup.find(text = re.compile(r"He's"))
        characters = re.match("He's.*(?=They fight crime!)", characters).group() # Using positive lookhead to keep character descriptions only
        male, female = re.split(" (?=She's)", characters)
        male_characters.write(male + "\n")
        female_characters.write(female + "\n")
        time.sleep(0.5) #To add a lag before the next request, added for precaution
    else:
        print(data.status_code)
        break

male_characters.close()
female_characters.close()   
