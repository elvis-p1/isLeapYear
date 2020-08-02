# a leap year is divisble by 4 while also divisible by 400 if divisible by 100
def isLeapYear(year):
    if year%4 == 0:
        if year%100 == 0: # the year cannot be divisible by 100 unless also divisible by 400
            if year%400 == 0:
                return True
            else:
                return False
        return True
    return False

# main function
# takes user input
def main():
    # check if the input is valid (an integer)
    try:
        user_input = int(input("Enter a year as an integer "))
        if isLeapYear(user_input):
            print("The year " + str(user_input) + " is a leap year")
        else:
            print("The year " + str(user_input) + " is not a leap year")
    except:
        # error message
        print("That was not an integer entered")

while True:
    main()
    