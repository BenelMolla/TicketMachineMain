from pharmacy import pharmacy
from perfumes import perfume
from cosmotiecs import cosmo
#from timercounter import timer


def main_data():
    place = int(input("choose your option: "))
    if place == 1:
        print("\n\t\t\t\t reservation")
        print("\t\t\t\tyour ticket number is:", "ph", next(perfume))
        print("""\t\t\t\tNow Take your ticket! thanks:
                                Date: 1 November 2022
                                Start time: \t20:21
                                End time: \t22:21\n
                                """)
        print("\n")
    elif place == 2:
        print("\n\t\t\t\t reservation")
        print("\t\t\t\tyour ticket number is:", "ph", next(pharmacy))
        print("""\t\t\t\tNow Take your ticket! thanks:
                        Date: 1 November 2022
                        Start time: \t20:21
                        End time: \t22:21\n
                        """)
        print("\n")

    elif place == 3:
        print("\n\t\t\t\t reservation")
        print("\t\t\t\tyour ticket number is:", "ph", next(cosmo))
        print("""\t\t\t\tNow Take your ticket! thanks:
                                Date: 1 November 2022
                                Start time: \t20:21
                                End time: \t22:21\n
                                """)
        print("\n")

    else:
        print("wrong choice")

    #timer()
