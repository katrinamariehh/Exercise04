def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """
    for i in range(2,len(input_list)-2):
        if i % 2 == 0:
            input_list[i] = 42
        elif i % 2 == 1:
            input_list[i] = 37

animals = ['pig', 'horse', 'narwhals', 'elephants', 'unicorns', 'balloonicorns', 'monkeys']


#for i in range(len(animals)-1,0,-1):
#        if animals[i] == "horse":
#            del animals[i]
#        else: 
#            print "Not a horse"

#print animals

#deleters = len(animals)
#animals.extend(animals[::-1])
#del animals[0:deleters]

print animals

#for i in range(len(animals)):
   # last_animal = animals.pop()
  #  animals[i:i] = [last_animal]
 #   i += 1
#print animals

for i in range((len(animals)/2)):
    endangeredspecies = animals[i]
    animals[i] = animals[-i-1]
    animals[-i-1] = endangeredspecies
    i += 1

print animals