from formatting import *


def analyzer(url="https://www.imdb.com/"):
    from requests import head

    try:
        head(url)
    except:
        print(colors('OPS: parece que o programa não pode ser usado nesse momento...', color='vermelho', ngr=True), end=" ")
        print(colors('Mas tente novamente mais tarde.', color='amareloc'))
        exit()


def director_or_creator(ID):
    from functions import Directors, Creators, Writers
    try:
        Directors(ID)
    except:
        Creators(ID)
    else:
        try:
            Writers(ID)
        except:
            print("Autor = Autor da obra pesquisada não encontrado.")


def movie_checker(title):
    # Pega o titulo do filme e converte em um ID.
    import imdb
    from system import info

    movie = imdb.IMDb()
    moviesDb = movie.search_movie(title)
    if len(moviesDb) == 0:
        print(colors(f"Não há filmes com esse título.", color='vermelho'))
    else:
        for pos, movie in enumerate(moviesDb):
            print(f"{pos+1} - {movie}")
        print()
        opt = number_checker(colors("Digite o número do filme que deseja ver as informações[0 para sair]:", color='amareloc'), len(moviesDb))
        print()
        if (opt-1) < 0:
            print(colors("Não achou o que procurava? Talvez você queira tentar novamente...", color='magenta', ngr=True))
        else:
            ID = moviesDb[opt-1].getID()
            info(ID)


def number_checker(ask, total):
    while True:
        try:
            nc = int(input(f"{ask}").strip())
        except (TypeError, ValueError):
            print(colors("ERRO: Valor digitado não é válido. Por favor, tente novamente...", color="vermelho"))
            continue
        if nc > total:
            print(colors(f"ERRO: Digite somente números entre 1 e {total}. Por favor, tente novamente...", color="vermelho"))
            continue
        return nc
