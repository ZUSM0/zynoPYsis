from system import *
from extra import *

movie = IMDb().get_movie('1129398').items()
for movies in movie:
    print(movies)
choose = ['Informações sobre um filme', 'Top 20 filmes do momento', 'Sair']
while True:
    header(colors("O QUE DESEJA VER?", color="verde", ngr=True))
    for num, c in enumerate(choose):
        print(f"{colors(num+1, color='verdec')} - {colors(c, color='azul')}")
    row(17)

    choice = number_checker(colors("Sua opção:", color='amareloc'), len(choose))

    if choice == 1:
        row(17)
        while True:
            title = input(colors("Digite o nome do filme:", color='ciano')).strip()
            print()
            info(title)

            rep = ""
            while rep == "":
                rep = input(colors("\nVocê deseja continuar?[S/N]", color='amareloc')).lower()
            if rep == "n":
                break

    elif choice == 2:
        row(17)
        print(colors("TOP 20 FILMES SÃO:"))
        print()
        Top_20()
        print()

    elif choice == 3:
        print(colors("\nObrigado por usar o programa!!!", color='verde'))
        break

#procurar API do google tradutor para traduzir as legendas caso o usuário do programa queira. Idéia de uma: Googletrans.pypi
#Formatar tudo com a biblioteca os depois
#planejar uma forma de limpar o console cada vez que não precisar de uma determinada parte exibindo(semelhante o que consegue fazer um c#)