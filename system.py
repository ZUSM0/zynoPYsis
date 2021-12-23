from functions import *
from extra import *


def top_10():
    topMovies = IMDb().get_popular100_movies()
    for cont, movies in enumerate(topMovies[0:10]):
        print(f"{cont+1} - {movies}")


def info(code):
    information = [Title(code), Year(code), Kind(code), Genre(code), Seasons(code), Rating(code), Cast(code),
                   director_or_creator(code)]
    for item in information:
        try:
            item

            # Title(code)
            # Year(code)
            # Kind(code)
            # Genre(code)
            # Seasons(code)
            # Rating(code)
            # Cast(code)
            # director_or_creator(code)
            # print()
            # Synopsis(code)

        except:
            try:
                pass
            except:
                print(colors(f"OPS: Parece que ainda não temos suporte sobre opção escolhida.", color='vermelho'))
                print(colors(f"Mas por favor, faça outra pesquisa...", color='amareloc'), end="\n")
