# Объект типа овощ - картошка

name = 'potatoes'
is_vegetable = True
diameter = 4
weight = 10.5

if is_vegetable:
    print('This vegetable is a ', end = '')
else:
    print('This fruit is a ', end = '')

print(name, '.', sep='')
print('It\'s weight = ', weight)
print('It\'s diameter = ', diameter)

print('Type variable name is', type(name))
print('Type is_vegetable name is', type(is_vegetable))
print('Type diameter name is', type(diameter))
print('Type weight name is', type(weight))