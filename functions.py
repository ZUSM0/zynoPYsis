from imdb import *
from formatting import *


def Seasons(ID):
    seasonsDb = IMDb().get_movie(ID)['seasons']
    print(f"{colors('Nº de temporadas:', color='azul')} {seasonsDb}")


def Kind(ID):
    kindDb = IMDb().get_movie(ID)['kind']
    print(f"{colors('Tipo:', color='azul')} {kindDb}")


def Genre(ID):
    #Verificar o genero do filme.
    genreDb = IMDb().get_movie(ID)['genres']
    try:
        print(f"{colors('Gênero: ', color='azul')}", end='')
        for cont, genre in enumerate(genreDb):
            if cont == 0:
                if len(genreDb) > 2:
                    print(f"{genre}", end="")
                elif len(genreDb) == 2:
                    print(f"{genre}", end="")
                else:
                    print(f"{genre}.")
            elif (cont + 1) < len(genreDb):
                print(f", {genre}", end="")
            else:
                print(f" e {genre}.")
    except:
        print(f"{colors('Gênero:', color='azul')} desconhecido")


def Rating(ID):
    #Verificar ID e retornar a avaliação do filme
    ratingDb = IMDb().get_movie(ID)['rating']
    try:
        print(f"{colors('Nota:', color='azul')} {ratingDb}/10")
    except:
        print(f"{colors('Nota:', color='azul')} sem avaliação no momento")


def Year(ID):
    #Retornar o ano de lançamento do filme.
    yearDb = IMDb().get_movie(ID)['year']
    try:
        print(f"{colors(f'Ano de lançamento:', color='azul')} {yearDb}")
    except:
        print(f"{colors(f'Ano de lançamento:', color='azul')} desconhecido")


def Title(ID):
    #retorna o nome do titulo.
    titleDb = IMDb().get_movie(ID)['title']
    LtitleDb = IMDb().get_movie(ID)['localized title']
    try:
        print(f"{colors('Titulo:', color='azul')} {LtitleDb}")
    except:
        print(f"{colors('Titulo:', color='azul')} {titleDb}")


def Writers(ID):
    writersDb = IMDb().get_movie(ID)['writer']
    for cont, writers in enumerate(writersDb):
        if cont == 0:
            if len(writersDb) > 2:
                print(f"{colors('Escritores:', color='azul')}: {writers}", end="")
            elif len(writersDb) == 2:
                print(f"{colors('Escritores:', color='azul')}: {writers}", end="")
            else:
                print(f"{colors('Escritores:', color='azul')}: {writers}.")
        elif (cont + 1) < len(writersDb):
            print(f", {writers}", end="")
        else:
            print(f" e {writers}.")


def Creators(ID):
    creatorsDb = IMDb().get_movie(ID)
    for cont, creators in enumerate(creatorsDb['creator']):
        if cont == 0:
            if len(creatorsDb['creator']) > 2:
                print(f"{colors('Criadores:', color='azul')}: {creators}", end="")
            elif len(creatorsDb['creator']) == 2:
                print(f"{colors('Criadores:', color='azul')}: {creators}", end="")
            else:
                print(f"{colors('Criadores:', color='azul')}: {creators}.")
        elif (cont + 1) < len(creatorsDb['creator']):
            print(f", {creators}", end="")
        else:
            print(f" e {creators}.")


def Directors(ID):
    directorsDb = IMDb().get_movie(ID)['directors']
    for cont, director in enumerate(directorsDb):
        if cont == 0:
            if len(directorsDb) > 2:
                print(f"{colors('Diretores:', color='azul')}: {director}", end=", ")
            elif len(directorsDb) == 2:
                print(f"{colors('Diretores:', color='azul')}: {director}", end=" ")
            else:
                print(f"{colors('Diretores:', color='azul')}: {director}.")
        elif (cont+1) < len(directorsDb):
            print(director, end=", ")
        else:
            print(f"e {director}.")


def Cast(ID):
    #pega o ID e mostra os atores do filme.
    actorsDb = IMDb().get_movie(ID)['cast']
    try:
        for cont, actor in enumerate(actorsDb):
            if cont == 0:
                if len(actorsDb) > 2:
                    print(f"Elenco: {actor}", end=", ")
                elif len(actorsDb) == 2:
                    print(f"Elenco: {actor}", end=" ")
                else:
                    print(f"Elenco: {actor}.")
            elif (cont+1) < len(actorsDb):
                print(actor, end=", ")
            else:
                print(f"e {actor}.")
    except:
        print("Elenco: sem informações do elenco")


def Synopsis(ID):
    #Pega um ID e mostrar a sinopse do filme.
    movie = IMDb().get_movie_synopsis(ID)
    print(f"'{movie['data']['plot'][0]}'")
