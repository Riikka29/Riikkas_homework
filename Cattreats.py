# Set the selected cat
SelectedCat = 'Snowball II'

# Create and fill lists of cats and treats
Cats = ['Garfield', 'Nermal', 'Tom Cat', 'Puss in Boots', 'Hobbes', 'Stimpy', 'Snowball II']
Treats = ['Lasagne', 'Praise', 'Mice', 'Power', 'Calvin', 'Fresh kitty litter', 'Fish']

# Find location of location selected cat
CatIndex = Cats.index(SelectedCat)

# Print cat name and favorit treat on screen
print("The favorite treat of", SelectedCat, "is", Treats[CatIndex])
