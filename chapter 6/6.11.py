'''Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.'''


cities = {}
n = int(input("How many cities are there to store : "))
for _ in range(n):
    cities_name = input("Enter city name : ")
    information = {}
    info_num = int(input("how mamy information you want to add in this city : "))
    for _ in range(info_num):
        info_name = input("Enter information name : ")
        info_detail = input("Enter information detail : ")
        information[info_name.title()] = info_detail
    cities[cities_name.title()] = information

for key , values in cities.items():
    print(f"{key.title()} : ")
    for key , value in values.items():
        print(f"\t{key} : {value}")