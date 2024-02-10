def Find():
    n = 50
    start = 0
    attempts = 7
    iterator = 0
    for i in range(1, attempts):
        print("Число <", n, "(Y - да, N - нет):")
        answer = input()
        iterator = iterator + 1
        if answer == "y" or answer == "Y":
            print("Число <", 25, "(Y - да, N - нет):")
            answer = input()
            iterator = iterator + 1
            if answer == "y" or answer == "Y":
                n = 25
                for j in range(i, attempts):
                    import random
                    random_number = random.randint(start, n)
                    print(random_number)
                    answer = input("Это:")
                    iterator = iterator + 1
                    if answer == "y" or answer == "Y":
                        print("Ура!")
                        return
                    if iterator == attempts:
                        print("Попытки кончились")
                        return
            else:
                start = 25
                n = 50
                for k in range(i, attempts):
                    import random
                    random_number = random.randint(start, n)
                    print(random_number)
                    answer = input("Это:")
                    iterator = iterator + 1
                    if answer == "y" or answer == "Y":
                        print("Ура!")
                        return
                    if iterator == attempts:
                        print("Попытки кончились")
                        return
        else:
            print("Число <", 75, "(Y - да, N - нет):")
            answer = input()
            iterator = iterator + 1
            if answer == "y" or answer == "Y":
                start = n
                n = 75
                for g in range(i, attempts):
                    import random
                    random_number = random.randint(start, n)
                    print(random_number)
                    answer = input("Это:")
                    iterator = iterator + 1
                    if answer == "y" or answer == "Y":
                        print("Ура!")
                        return
                    if iterator == attempts:
                        print("Попытки кончились")
                        return
            else:
                start = 75
                n = 100
                for h in range(i, attempts):
                    import random
                    random_number = random.randint(start, n)
                    print(random_number)
                    answer = input("Это:")
                    iterator = iterator + 1
                    if answer == "y" or answer == "Y":
                        print("Ура!")
                        return
                    if iterator == attempts:
                        print("Попытки кончились")
                        return
    if iterator == attempts:
        print("Попытки кончились")
        return


Find()
