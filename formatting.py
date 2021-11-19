def row(n):
    print("~~" * n)


def header(msg, acr=0):
    row(17)
    print(f"{msg}".center(32))
    row(17)


def colors(msg, color="black".lower(), ngr=False):
    if ngr:
        ngr = 1

    elif ngr == False:
        ngr = 0

    if color == "vermelho":
        return f"\033[{ngr};31m{msg}\033[m"

    elif color == "verde":
        return f"\033[{ngr};32m{msg}\033[m"

    elif color == "amarelo":
        return f"\033[{ngr};33m{msg}\033[m"

    elif color == "azul":
        return f"\033[{ngr};34m{msg}\033[m"

    elif color == "magenta":
        return f"\033[{ngr};35m{msg}\033[m"

    elif color == "ciano":
        return f"\033[{ngr};36m{msg}\033[m"

    elif color == "cinza claro":
        return f"\033[{ngr};37m{msg}\033[m"

    elif color == "verdec":
        return f"\033[{ngr};92m{msg}\033[m"

    elif color == "amareloc":
        return f"\033[{ngr};93m{msg}\033[m"

    elif color == "azulc":
        return f"\033[{ngr};94m{msg}\033[m"
    else:
        return f"\033[{ngr}m{msg}\033[m"
