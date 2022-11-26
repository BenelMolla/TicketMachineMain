from maindata import main_data
from countdown import countdown


def timer():
    print("Hi welcome to our drug store: ")
    print("where you want to go:")
    print("\t1, perfumery")
    print("\t2, Pharmaceuticals")
    print("\t3, Cosmetics")
    ID = [346549306, 346369432]
    count = 0
    user = int(input("please enter your id:   "))
    while count < 2:
        if user in ID:
            print("\t\t\t\t\t\tyou are registered, welcome and select your destination")
            main_data()
        else:
            print("\t\t\t\t\t\tyou are not rigistered, sorry")
            user = int(input("please enter your id:   "))
            count += 1
    else:
        print("\t\t\t\t\t\tyou are now BLOCKED for 5 sec, sorry")
        print("sorry u have to stay for 5 sec to try again")
        countdown(int(5))


timer()
