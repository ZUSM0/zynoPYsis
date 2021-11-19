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


def info(ttl):
    code = id_checker(ttl)
    #Organizar essa parte para ficar como se fosse um menuzinho com informações sobre o filme.
    #Só estetica, pois o código completo

    try:
        print()
        kind = Kind(code)
        if kind == 'movie':
            print(f'''O título do filme é {Title(code)}''')

        elif kind == 'tv series':
            print("è uma serie de tv")
            director_or_creator(code)

        elif kind == 'tv mini series':
            pass
        # Rating(code)
        #
        # Year(code)
        # Genre(code)
        # print()
        # #
        # print()
        # Cast(code)
        # print()
        # Synopsis(code)
        else:
            print(colors(f"OPS: Parece que ainda não temos informações sobre o que você procurou.", color='vermelho'))
            print(colors(f"Mas por favor, faça outra pesquisa...", color='amareloc'), end=" ")
    except (TypeError):
        print(colors("Não achou o que procurava? Talvez você queira tentar novamente...", color='magenta'))