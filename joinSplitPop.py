#source learn python of the hard way

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things in that list, let's fix that."
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff


# print "Let's do some things with stuff."
print
print stuff[1]
print  stuff[- 1] # whoa! fancy
print  stuff.pop()
print  ' '.join(stuff) # what? cool!
print  '#'.join(stuff[3:5]) # super stellar!

## Results
## Wait there's not 10 things in that list, let's fix that.
## Adding:  Boy
## There's 7 items now.
## Adding:  Girl
## There's 8 items now.
## Adding:  Banana
## There's 9 items now.
## Adding:  Corn
## There's 10 items now.
## There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
##
## Oranges
## Corn
## Corn
## Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
## Telephone#Light
