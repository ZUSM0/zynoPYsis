from formatting import *

#resolver a questão do system e fazer os tratamentos de erro(para quando não encontrar nenhum filme por exemplo)

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


def id_checker(title):
    # Pega o titulo do filme e converte em um ID.
    import imdb

    movie = imdb.IMDb()
    moviesDb = movie.search_movie(title)
    for pos, movie in enumerate(moviesDb):
        print(f"{pos+1} - {movie}")
    print()
    opt = number_checker(colors("Digite o número do filme que deseja ver as informações[0 para sair]:", color='amareloc'), len(moviesDb))
    if (opt-1) < 0:
        pass
    else:
        print(moviesDb[opt-1].getID())
        return f"{moviesDb[opt-1].getID()}"


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
