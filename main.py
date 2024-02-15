def For(i, attempts, iterator, n, start):
    import random
    for j in range(i, attempts):
        random_number = random.randint(start, n)
        print("Это", random_number, "?")
        answer = input()
        iterator = iterator + 1
        if answer == "y" or answer == "Y":
            print("Ура!")
            return
        if iterator == attempts:
            print("Попытки кончились")
            return


def Find():
    attempts = 7
    iterator = 0
    for i in range(1, attempts):
        print("Число <", 50, "(Y - да, N - нет):")
        answer = input()
        iterator = iterator + 1
        if answer == "y" or answer == "Y":
            print("Число <", 25, "(Y - да, N - нет):")
            answer = input()
            iterator = iterator + 1
            if answer == "y" or answer == "Y":
                print("Число <", 15, "(Y - да, N - нет):")
                answer = input()
                iterator = iterator + 1
                if answer == "y" or answer == "Y":
                    For(i, attempts, iterator, n=15, start=0)
                    return
                else:
                    For(i, attempts, iterator, n=25, start=15)
                    return
            else:
                print("Число <", 35, "(Y - да, N - нет):")
                answer = input()
                iterator = iterator + 1
                if answer == "y" or answer == "Y":
                    For(i, attempts, iterator, n=35, start=25)
                    return
                else:
                    For(i, attempts, iterator, n=50, start=35)
                    return
        else:
            print("Число <", 75, "(Y - да, N - нет):")
            answer = input()
            iterator = iterator + 1
            if answer == "y" or answer == "Y":
                For(i, attempts, iterator, n=75, start=50)
                return
            else:
                print("Число <", 90, "(Y - да, N - нет):")
                answer = input()
                iterator = iterator + 1
                if answer == "y" or answer == "Y":
                    For(i, attempts, iterator, n=90, start=75)
                    return
                else:
                    For(i, attempts, iterator, n=100, start=90)
                    return
    if iterator == attempts:
        print("Попытки кончились")
        return


Find()
print("Игра окончена")
