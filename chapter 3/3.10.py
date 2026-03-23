'''Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.'''

fav_place = ['russia','America','Canada','My home']
print(fav_place[0])
fav_place[2] = 'Spain'
print(fav_place)
fav_place.append('Thailand')
print(fav_place)
fav_place.insert(1,'Paris')
print(fav_place)
fav_place.extend(['Germany'])
print(fav_place)
another = ['Japan']
fav_place.extend(another)
print(fav_place)
fav_place.remove('Spain')
print(fav_place)
del fav_place[5]
print(fav_place)
print(sorted(fav_place))
print(sorted(fav_place,reverse=True))
print(fav_place)
fav_place.reverse()
print(fav_place)
fav_place.reverse()
print(fav_place)
fav_place.sort()
print(fav_place)
fav_place.sort(reverse=True)
print(fav_place)
fav_place.sort()
print(fav_place)