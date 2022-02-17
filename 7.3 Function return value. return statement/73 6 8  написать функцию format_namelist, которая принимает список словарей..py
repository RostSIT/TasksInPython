def format_namelist(dictionary):
    string = ''
    b = ', '
    a = ' и '
    for key, value in dictionary.items():
        if len(dictionary) == 3:
            string+= value
        if len(dictionary) == 2:
            string += dictionary[0] + a + dictionary[1]
        if len(dictionary) == 1:
            string += dictionary[0]
    return string


print(format_namelist({'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}))
print(format_namelist({'name': 'Bart'}, {'name': 'Lisa'}))
print(format_namelist({'name': 'Bart'}))
