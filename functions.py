from imdb import *


def Seasons(ID):
    seasonsDb = IMDb().get_movie(ID)['seasons']
    return seasonsDb


def Kind(ID):
    kindDb = IMDb().get_movie(ID)['kind']
    return kindDb


def Genre(ID):
    #Verificar o genero do filme.
    genreDb = IMDb().get_movie(ID)['genres']
    return genreDb


def Rating(ID):
    #Verificar ID e retornar a avaliação do filme
    ratingDb = IMDb().get_movie(ID)['rating']
    return ratingDb


def Year(ID):
    #Retornar o ano de lançamento do filme.
    yearDb = IMDb().get_movie(ID)['year']
    return yearDb


def Title(ID):
    #retorna o nome do titulo. Depois decidir se pega o titulo original em inglês("original title")
    # ou o titulo em portugues("localized title")
    OrigtitleDb = IMDb().get_movie(ID)['original title']
    LocaltitleDb = IMDb().get_movie(ID)['localized title']
    print(OrigtitleDb)


def Writers(ID):
    writersDb = IMDb().get_movie(ID)['writer']
    for cont, writers in enumerate(writersDb):
        if cont == 0:
            if len(writersDb) > 2:
                print(f"Escritores = {writers}", end=", ")
            elif len(writersDb) == 2:
                print(f"Escritores = {writers}", end=" ")
            else:
                print(f"Escritores = {writers}.")
        elif (cont + 1) < len(writersDb):
            print(writers, end=", ")
        else:
            print(f"e {writers}.")

def Creators(ID):
    creatorsDb = IMDb().get_movie(ID)
    for cont, creators in enumerate(creatorsDb['creator']):
        if cont == 0:
            if len(creatorsDb['creator']) > 2:
                print(f"Criadores = {creators}", end=", ")
            elif len(creatorsDb['creator']) == 2:
                print(f"Criadores = {creators}", end=" ")
            else:
                print(f"Criador = {creators}.")
        elif (cont + 1) < len(creatorsDb['creator']):
            print(creators, end=", ")
        else:
            print(f"e {creators}.")


def Directors(ID):
    directorsDb = IMDb().get_movie(ID)['directors']
    for cont, director in enumerate(directorsDb):
        if cont == 0:
            if len(directorsDb) > 2:
                print(f"Diretores = {director}", end=", ")
            elif len(directorsDb) == 2:
                print(f"Diretores = {director}", end=" ")
            else:
                print(f"Diretor = {director}.")
        elif (cont+1) < len(directorsDb):
            print(director, end=", ")
        else:
            print(f"e {director}.")


def Cast(ID):
    #pega o ID e mostra os atores do filme.
    actorsDb = IMDb().get_movie(ID)['cast']
    for cont, actor in enumerate(actorsDb):
        if cont == 0:
            if len(actorsDb) > 2:
                print(f"Elenco = {actor}", end=", ")
            elif len(actorsDb) == 2:
                print(f"Elenco = {actor}", end=" ")
            else:
                print(f"Actors = {actor}.")
        elif (cont+1) < len(actorsDb):
            print(actor, end=", ")
        else:
            print(f"e {actor}.")


def Synopsis(ID):
    #Pega um ID e mostrar a sinopse do filme.
    movie = IMDb().get_movie_synopsis(ID)
    print(f"'{movie['data']['plot'][0]}'")
