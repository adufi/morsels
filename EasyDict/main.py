from EasyDict import EasyDict

#
ed = EasyDict({'name': 'Arnaud', 'location': 'Martinique'})

#
ed = EasyDict(name='Arnaud', location='Martinique')

#
print (ed.name)

#
ed['location'] = 'San Diego'
print (ed['location'])

#
print (ed == EasyDict(name='Arnaud', location='San Diego'))
print (ed == EasyDict(name="Trey Hunner", location="San Diego"))

#
print (ed.get('profession'))
print (ed.get('profession', 'unknown'))
print (ed.get('name', 'unknown'))

#
ed = EasyDict({'greeting 1': 'Hello World'}, normalize=True)
print (ed['greeting_1'])

