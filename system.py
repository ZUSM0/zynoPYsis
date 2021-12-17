from functions import *
from extra import *

def top_10():
    topMovies = IMDb().get_popular100_movies()
    for cont, movies in enumerate(topMovies[0:10]):
        print(f"{cont+1} - {movies}")


def info(code):

    print(Kind(code))
    if Kind(code) == 'movie':
        print(f"{colors('O titulo do filme é:', color='azul')} {Title(code)}")
        print(f"{colors(f'Ano de lançamento:', color='azul')} {Year(code)}")
        print(f"{colors('Gênero:', color='azul')}", end='')
        Genre(code)
        print(f"{colors('Nota:', color='azul')} {Rating(code)}/10")
        print()
        Synopsis(code)

    elif Kind(code) == 'tv series':
        print(f"{colors('O titulo do série é:', color='azul')} {Title(code)}")

    elif Kind(code) == 'tv mini series':
        print(f"{colors('O titulo do minissérie é:', color='azul')} {Title(code)}")

    else:
        print(colors(f"OPS: Parece que ainda não temos informações sobre opção escolhida.", color='vermelho'))
        print(colors(f"Mas por favor, faça outra pesquisa...", color='amareloc'), end="\n")
