import requests
from bs4 import BeautifulSoup
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file_name", type=str, default="output", help="name of the output file")
args = parser.parse_args()

url = 'https://www.filmweb.pl/ranking/film'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
main_div = soup.find('div', class_ = 'page__container rankingTypeSection__container')

movie_data_odd = main_div.find_all('div', class_ = 'rankingType--odd')
movie_data_even = main_div.find_all('div', class_ = 'rankingType--even')

movies = movie_data_odd + movie_data_even
movies_list = []

for movie in movies:
    basics = movie.find('h2').text.strip()
    parts = basics.split('. ', 1)
    number = int(parts[0])
    title = parts[1]

    title_eng = movie.find('p').text.strip()
    *title_parts, year = title_eng.rsplit(' ', 1)
    title_eng = ' '.join(title_parts)
    
    rate = movie.find('span', class_='rankingType__rate--value').text.strip()
    genre = movie.find('a', class_='rankingGerne').text.strip()

    # print(f'{number=}')
    # print(f'{title=}')
    # print(f'{title_eng=}')
    # print(f'{year=}')
    # print(f'{rate=}')
    # print(f'{genre=}')
    # print('-----------------')
    movies_list.append({
        'number': number,
        'title': title,
        'title_eng': title_eng,
        'year': year,
        'rate': rate,
        'genre': genre
    })

movies_list.sort(key=lambda x: x['number'])

# print(json.dumps(movies_list, indent=4, ensure_ascii=False))

file_name = 'projects/005/' + args.file_name + '.json'
print(f'Saving data to {file_name}')

with open(file_name, 'w') as file:
    json.dump(movies_list, file, indent=4)