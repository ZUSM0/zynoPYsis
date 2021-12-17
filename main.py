from system import *
from extra import *

choose = ['Informações sobre um filme', 'Top 10 filmes do momento', 'Sair']
while True:
    header(colors("O QUE DESEJA VER?", color="verde", ngr=True))
    for num, c in enumerate(choose):
        print(f"{colors(num+1, color='verdec')} - {colors(c, color='azul')}")
    row(17)

    choice = number_checker(colors("Sua opção:", color='amareloc'), len(choose))
    analyzer()

    #usar a função header para colocar os titulos
    if choice == 1:
        header(colors("ZynoPysis", color='azul'))
        while True:
            title = input(colors("Digite o nome do filme:", color='ciano')).strip()
            print()
            movie_checker(title)
            #mudei pra chamar a função info depois que saber se o resultado foi certo ou não(id chcker primeiro depois info e etc)
            rep = ""
            while rep == "":
                rep = input(colors("\nVocê deseja continuar?[S/N]", color='amareloc')).lower()
            if rep == "n":
                break

    elif choice == 2:
        header(colors("TOP 10 FILMES SÃO:",color='azul'))
        print()
        top_10()
        print()

    elif choice == 3:
        print(colors("\nObrigado por usar o programa!!!", color='verde'))
        break
