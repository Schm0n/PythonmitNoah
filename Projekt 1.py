from random import shuffle
lower = 0
upper = 0
answer = 0

def randomNumber(lower, upper):
    list = [lower]
    while list[-1] != upper:
        list.append(list[-1]+1)
    shuffle(list)
    gesucht = int(list[-1])
    return gesucht


def answerdef (lower, upper):
    try: answer = int(input(f"errate die Zahl in der Grenze {lower} und {upper}:\n"))
    except ValueError:
        answer = int(input(f"errate die Zahl! in der Grenze {lower} und {upper}:\n"))
    return answer


def hint(answer, gesucht):
    while answer != gesucht:
        if answer < gesucht:
            try: answer = int(input(f"die gesuchte Zahl ist größer {answer}\n"))
            except ValueError:
                answer = int(input(f"die gesuchte Zahl! ist größer {answer}\n"))
        elif answer > gesucht:
            try: answer = int(input(f"die gesuchte Zahl ist kleiner {answer}\n"))
            except ValueError:
                answer = int(input(f"die gesuchte Zahl! ist kleiner {answer}\n"))
    if answer == gesucht:
        print(f"Herzlichen glückwunsch du hast die gesuchte Zahl {gesucht} gefunden!")


def unten():
    try: lower = int(input("bestimme eine untere Grenze:\n"))
    except ValueError:
        lower = int(input("bestimme eine Zahl als untere Grenze:\n"))
    return lower


def oben(lower):
    try: upper = int(input("bestimme eine obere Grenze:\n"))
    except ValueError:
        upper = int(input("bestimme eine Zahl als obere Grenze:\n"))
    while lower > upper:
        try: upper = int(input("die obere Grenze muss größer als die untere Grenze sein!\nbestimme eine obere Grenze\n"))
        except ValueError:
            upper = int(input("die obere Grenze muss eine Zahl und größer als die untere Grenze sein!\nbestimme eine obere Grenze\n"))
    return upper


def main(lower, upper, answer):
    lower = unten()
    upper = oben(lower)
    gesucht = int(randomNumber(lower, upper))
    answer = int(answerdef(lower, upper))
    hint(answer, gesucht)


main(lower, upper, answer)

#replay option
#fix wenn != int eingegeben werden
