from functions import *
from extra import *

# def sugestões():
#Vai precisar de um tradutor no futuro
#     #Colocar um menu de sugestão de filmes com base em alguma palavra chave
#     # movie = IMDb().get_keyword('school')
#     # for movies in movie:
#     #     print(movies)
#     #


def Top_20():
    TopMovies = IMDb().get_popular100_movies()
    for cont, movies in enumerate(TopMovies[0:20]):
        print(f"{cont+1} - {movies}")


def info(code):

    try:
        title = Title(code)
        year = Year(code)
        season = Seasons(code)
        kind = Kind(code)
        genre = Genre(code)
        rating = Rating(code)
        synop = Synopsis(code)

        if kind == 'movie':
            print(f"{colors('O titulo do filme é:', color='azul')} {title}")

        elif kind == 'tv series':
            print(f"{colors('O titulo do série é:', color='azul')} {title}")

        elif kind == 'tv mini series':
            print(f"{colors('O titulo do minissérie é:', color='azul')} {title}")

        else:
            print(colors(f"OPS: Parece que ainda não temos informações a opção escolhida.", color='vermelho'))
            print(colors(f"Mas por favor, faça outra pesquisa...", color='amareloc'), end=" ")

    except (TypeError):
        print(colors("Não achou o que procurava? Talvez você queira tentar novamente...", color='magenta', ngr=True))