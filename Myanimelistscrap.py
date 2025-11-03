from bs4 import BeautifulSoup
import requests
import re
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)



url = 'https://myanimelist.net/topanime.php'
base_url = 'https://myanimelist.net/topanime.php?limit='
'''

result = requests.get(url)
soup = BeautifulSoup(result.content,'html.parser')
tr = soup.find_all('h3',class_="fl-l fs14 fw-b anime_ranking_h3")
flex_class = re.compile(r"text on score-label score-\d")
rating = soup.find_all('span',class_= flex_class )
'''

for i in range(0,100,50):
    new_url = base_url + str(i)
    res = requests.get(new_url)
    soup = BeautifulSoup(res.content,'html.parser')
    anime_list = soup.find_all('h3',class_="fl-l fs14 fw-b anime_ranking_h3")
    flex_class = re.compile(r"text on score-label score-\d+")
    rating = soup.find_all('span',class_= flex_class )
    print('='*30)
    print(f'Top anime {i+1} - {i+50}')
    for anime,rate in zip(anime_list,rating):
        print('=' * 30)
        print(anime.get_text(strip = True))
        print(f'{rate.text}⭐')
        
        




