# title() - The title() method returns a string where the first character in every word is upper
# case. Like a header, or a title. If the word contains a number or a symbol, the first letter after that will be
# converted to upper case."""

# the capitalize() method returns a copy of the original string and converts the first character of the string to a
# capital (uppercase) letter while making all other characters in the string lowercase letters.


def print_initials(name, surname, middlename):
    print(f'{surname.capitalize()} {name[0].capitalize()}.{middlename[0].title()}.')


print_initials('евгЕний', 'петросян', 'ВаГАнович')
