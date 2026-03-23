''' Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.'''

def city_country(city,country="India"):
    return f"\"{city.title()}, {country.title()}\""

print(city_country("narnaul"))
print(city_country(city="new york",country="america"))
print(city_country(city="seoul",country="south korea"))
