from random import shuffle


def randomNumber(lower, upper):
    list = [lower]
    while list[-1] != upper:
        list.append(list[-1]+1)
    shuffle(list)
    suche = int(list[-1])
    gesucht = int(suche)

    print(gesucht)
    print(list)
    return gesucht


def answerdef (lower, upper):
    antwort = int(input(f"errate die Zahl in der Grenze {lower} und {upper}:\n"))
    answer = int(antwort)
    print(answer)
    return answer


def hint(answer, gesucht):
    while answer != gesucht:
        if answer < gesucht:
            answer = int(input(f"die gesuchte Zahl ist größer {answer}\n"))
        elif answer > gesucht:
            answer = int(input(f"die gesuchte Zahl ist kleiner {answer}\n"))
    if answer == gesucht:
        print(f"Herzlichen glückwunsch du hast die gesuchte Zahl {gesucht} gefunden!")



#def grenzen():


def main(lower, upper, answer, gesucht):
    lower = int(input("bestimme eine untere Grenze:\n"))
    upper = int(input("bestimme eine obere Grenze:\n"))
    while lower > upper:
        upper = input("die obere Grenze muss größer als die untere Grenze sein!\nbestimme eine obere Grenze\n")
    print(lower)
    print(upper)
    randomNumber(lower, upper)
    answerdef(lower, upper)
    hint(answer, gesucht)


def spiel():
    lower = 0
    upper = 0
    answer = 0
    gesucht = 0
    main(lower, upper, answer, gesucht)


spiel()





























#def main():
    #grenzen()
    #randomNumber()
    #userInput()
    #hint()