from bs4 import BeautifulSoup
import requests


games = []

def GetGames(page = 1):
    site = f'https://www.pushsquare.com/games/browse?system=psp&page={page}'
    currentPage = 1

    page = requests.get(site)

    print(page.text)
    t = page.text

    soup = BeautifulSoup(page.content,'html.parser')

    results = soup.find_all("li", class_="item item-content item-game")

    print('\n', len(results))
    # print('\n', results)

    for i in results:
        print(i)
        s = str(i)
        gameIndex = s.find('/games/psp/')
        print(gameIndex)
        print(s[gameIndex])

        game = ''
        currentLetter = s[gameIndex]
        while currentLetter != '>':
            game+=currentLetter

            gameIndex += 1
            currentLetter = s[gameIndex]
        
        game = game.replace('"', '') #tira o " do final
        print(game)
        games.append(game)


GetGames(1)
print(games)

# with open('coiso.txt', 'w', errors='ignore') as coiso:
#     #for i in t:
#     #    print(i)
#     coiso.write(page.text)