def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True

    elif year % 400 == 0:
        return True

    elif year % 100 == 0:
        return False

    else:
        return False

def checkLeapYear():
    while True:
        try:
            year = int(input("Enter year between 0-9999: "))
            if 0 <= year <= 9999:
                break
            raise ValueError()

        except ValueError:
            print("Enter number between 0 and 9999")

    if year %4 == 0 and year % 100 != 0:
        print(year, "is a leap year")
    
    elif year % 400 == 0:
        print(year, "is a leap year")
    
    elif year % 100 == 0:
        print(year, "is not a leap year")
    
    else:
        print(year, "is not a leap year")

checkLeapYear()