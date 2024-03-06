class InvalidAgeException(Exception):
    pass
num = 18

try:
    input_num = int(input('Enter Age : '))
    if input_num  < num:
        raise InvalidAgeException
    else:
        print('Age is Eligible for Voting')

except InvalidAgeException:
    print('Error : Invalid Age...')
