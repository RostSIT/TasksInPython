def format_namelist(dictionary):
    string = ''
    d = []
    a = ' и '
    c = ', '
    for i in range(len(dictionary)):
        d.append(dictionary[i]['name'])
    if len(d) == 3:
        for i in range(len(d) - 1):
            string += str(d[i])
            c.join(string)
        string += a + str(d[2])
        return string

    if len(d) == 2:
        string = a.join(d)
        return string
    if len(d) == 1:
        return string.join(d)
    if len(d) == 0:
        return string


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(format_namelist([{'name': 'Bart'}]))
print(format_namelist([]))
# for key, value in dictionary.items():


#         if len(dictionary) == 3:
#             string+= value
#         if len(dictionary) == 2:
#             string += dictionary[0] + a + dictionary[1]
#         if len(dictionary) == 1:
#             string += dictionary[0]
#     return string
#
#
# print(format_namelist({'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}))
# print(format_namelist({'name': 'Bart'}, {'name': 'Lisa'}))
# print(format_namelist({'name': 'Bart'}))
format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
