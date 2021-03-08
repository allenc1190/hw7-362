def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return False

    elif year % 400 == 0:
        return False

    elif year % 100 == 0:
        return True

    else:
        return True