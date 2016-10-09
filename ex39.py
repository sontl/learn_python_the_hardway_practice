# Dictionary

# create a mapping o state 
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA'
}

for key, val in states.items():
    print key, val

print "*" * 10
print states.get('Florida')
print "*" * 10
print states['Florida']
print "*" * 10
print states.get('Hanoi', 'Deo co thanh pho nhu the')