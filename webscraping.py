from ast import Break
from bs4  import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    movies = soup.find('tbody', class_="lister-list").find_all("tr")
    

    for movie in movies:

       

        name = movie.find('td', class_="titleColumn").a.text

        rating = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0] 

        Year = movie.find('td', class_="titleColumn").span.text.strip('()')

        imRating = movie.find('td', class_="ratingColumn imdbRating").strong.text

        print(name,rating,Year,imRating)
        

        
        

except Exception as e:
    print(e)