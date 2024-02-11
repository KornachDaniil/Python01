def For(i, attempts, iterator, n, start):
    last_number = 0
    for j in range(i, attempts):
        import random
        random_number = random.randint(start, n)
        last_number = random_number
        if last_number == random_number:
            random_number = random.randint(start, n)
            last_number = random_number
        print("Это", last_number, "?")
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
                For(i, attempts, iterator, n=25, start=0)
                return
            else:
                For(i, attempts, iterator, n=50, start=25)
                return
        else:
            print("Число <", 75, "(Y - да, N - нет):")
            answer = input()
            iterator = iterator + 1
            if answer == "y" or answer == "Y":
                For(i, attempts, iterator, n=75, start=50)
                return
            else:
                For(i, attempts, iterator, n=100, start=75)
                return
    if iterator == attempts:
        print("Попытки кончились")
        return


Find()
print("Игра окончена")
