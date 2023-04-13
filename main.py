from pprint import pprint
import requests


def test_request():
    
    url = "https://akabab.github.io/superhero-api/api/all.json"
    
    response = requests.get(url)
    data = response.json()
    heroes =  {}
    for super_hero in data:
        if super_hero['name'] == "Hulk" :
            heroes[super_hero['name']] = super_hero["powerstats"]['intelligence']
        elif super_hero['name'] == "Captain America":
            heroes[super_hero['name']] = super_hero["powerstats"]['intelligence']
        elif super_hero['name'] == "Thanos":
            heroes[super_hero['name']] = super_hero["powerstats"]['intelligence']
    
    heroes_sort = sorted(heroes.items(), reverse=True)

    print(*heroes_sort[0])
    
if __name__ == '__main__':
    test_request()

