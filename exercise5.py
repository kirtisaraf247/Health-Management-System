def getdate():
    import datetime
    return datetime.datetime.now()


def enterdiet(client):
    f = open(client + 'diet.txt')
    print('Enter diet for' + client)
    data = input('What has ' + client + ' eaten?: ')
    f.write([str(getdate())] + ' ' + data + '\n')
    f.close()


def enterexercise(client):
    f = open(client + 'ex.txt')
    print('Enter exercise for' + client)
    data = input('What exercise did ' + client + ' done?: ')
    f.write([str(getdate())] + ' ' + data + '\n')
    f.close()


def retrievediet(client):
    f = open(client + 'diet.txt')
    print(f.readlines())
    f.close()


def retrieveexercise(client):
    f = open(client + 'ex.txt')
    print(f.readlines())
    f.close()


print('Enter Client')
client = int(input(' 1.Harry\n 2.Rohan\n 3.Hammad\n'))
if client==1:
    print('Enter your choice: ')
    choice = int(input(' 1.Enter\n 2.Retrieve\n'))
    print('Enter your choice: ')
    choice1 = int(input(' 1.Diet\n 2.Exercise\n'))
    if choice==1 and choice1==1:
        enterdiet()
    elif choice==1 and choice1==2:
        enterexercise()
    elif choice == 1 and choice1 == 1:
        retrievediet()
    elif choice == 2 and choice1 == 2:
        retrieveexercise()

if client==2:
    print('Enter your choice: ')
    choice = int(input(' 1.Enter\n 2.Retrieve\n'))
    print('Enter your choice: ')
    choice1 = int(input(' 1.Diet\n 2.Exercise\n'))
    if choice==1 and choice1==1:
        enterdiet()
    elif choice==1 and choice1==2:
        enterexercise()
    elif choice == 1 and choice1 == 1:
        retrievediet()
    elif choice == 2 and choice1 == 2:
        retrieveexercise()

if client==3:
    print('Enter your choice: ')
    choice = int(input(' 1.Enter\n 2.Retrieve\n'))
    print('Enter your choice: ')
    choice1 = int(input(' 1.Diet\n 2.Exercise\n'))
    if choice==1 and choice1==1:
        enterdiet()
    elif choice==1 and choice1==2:
        enterexercise()
    elif choice == 1 and choice1 == 1:
        retrievediet()
    elif choice == 2 and choice1 == 2:
        retrieveexercise()