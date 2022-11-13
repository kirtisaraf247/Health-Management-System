def gettime():
    import datetime
    return datetime.datetime.now()


def log():
    print('Enter Client')
    client = int(input(' 1.Harry\n 2.Rohan\n 3.Hammad\n'))
    con = 1
    if client == 1:
        while con == 1:
            print('Enter choice: ')
            choice = int(input(' 1.Diet\n 2.Exercise'))
            if choice == 1:
                with open("harrydiet.txt", "w") as f:
                    data = str(input('Enter what has Harry eaten: '))
                    f.write(str([str(gettime())]) + "  " + data + "\n")
            else:
                with open("harryex.txt", "w") as f:
                    data = str(input("Enter Harry's exercise: "))
                    f.write(str([str(gettime())]) + "  " + data + "\n")
            con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))

    elif client == 2:
        while con == 1:
            print('Enter choice: ')
            choice = int(input(' 1.Diet\n 2.Exercise'))
            if choice == 1:
                with open("rohandiet.txt", "w") as f:
                    data = str(input('Enter what has Rohan eaten: '))
                    f.write(str([str(gettime())]) + "  " + data + "\n")
            else:
                with open("rohanex.txt", "w") as f:
                    data = str(input("Enter Rohan's exercise: "))
                    f.write(str([str(gettime())]) + "  " + data + "\n")
            con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))

    elif client == 3:
        while con == 1:
            print('Enter choice: ')
            choice = int(input(' 1.Diet\n 2.Exercise'))
            if choice == 1:
                with open("hammaddiet.txt", "w") as f:
                    data = str(input('Enter what has Hammad eaten: '))
                    f.write(str([str(gettime())]) + "  " + data + "\n")
            else:
                with open("hammadex.txt", "w") as f:
                    data = str(input("Enter Hammad's exercise: "))
                    f.write(str([str(gettime())]) + "  " + data + "\n")
            con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))


def retrieve():
    con = 1
    while con == 1:
        print('Enter Client')
        client = int(input(' 1.Harry\n 2.Rohan\n 3.Hammad\n'))
        if client == 1:
            print('Enter choice: ')
            choice = int(input(' 1.Diet\n 2.Exercise'))
            if choice == 1:
                with open("harrydiet.txt") as f:
                    print(f.readlines())
            else:
                with open("harryex.txt") as f:
                    print(f.readlines())

        if client == 2:
            print('Enter choice: ')
            choice = int(input(' 1.Diet\n 2.Exercise'))
            if choice == 1:
                with open("rohandiet.txt") as f:
                    print(f.readlines())
            else:
                with open("rohanex.txt") as f:
                    print(f.readlines())

        elif client == 3:
            print('Enter choice: ')
            choice = int(input(' 1.Diet\n 2.Exercise'))
            if choice == 1:
                with open("hammaddiet.txt") as f:
                    print(f.readlines())
            else:
                with open("hammadex.txt") as f:
                    print(f.readlines())
        con = int(input("Do you want to retrieve any more details? \n1. Yes \n2. No"))


print("------------Welcome to Health care Management System---------------")
ch = int(input("What do you want to do? \n1. Log \n2. Retrieve\n"))
if ch == 1:
    log()
elif ch == 2:
    retrieve()
else:
    print("Wrong Input. Please try again.")
