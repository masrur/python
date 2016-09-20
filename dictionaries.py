

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'

}
# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'

}
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities
print '- ' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
# print some states
print '- ' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
# do it by using the state then cities dict
print '- ' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
# print every state abbreviation
print '- ' * 10

# item selected as item()
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
    # print every city in state
print '- ' * 10

for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
    # now do both at the same time
print '- ' * 10
for state, abbrev in states.items():
   print "%s state is abbreviated %s and has city %s" % (
       state, abbrev, cities[abbrev]
   )


print '- ' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)
if not state:
    print "Sorry, no Texas."
    # get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
- - - - - - - - - - 
NY State has:  New York
OR State has:  Portland
- - - - - - - - - - 
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
- - - - - - - - - - 
Michigan has:  Detroit
Florida has:  Jacksonville
- - - - - - - - - - 
California is abbreviated CA
Michigan is abbreviated MI
New York is abbreviated NY
Florida is abbreviated FL
Oregon is abbreviated OR
- - - - - - - - - - 
FL has the city Jacksonville
CA has the city San Francisco
MI has the city Detroit
OR has the city Portland
NY has the city New York
- - - - - - - - - - 
California state is abbreviated CA and has city San Francisco
Michigan state is abbreviated MI and has city Detroit
New York state is abbreviated NY and has city New York
Florida state is abbreviated FL and has city Jacksonville
Oregon state is abbreviated OR and has city Portland
- - - - - - - - - - 
Sorry, no Texas.
The city for the state 'TX' is: Does Not Exist
