travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


# Write the function that will allow new countries
# to be added to the travel_log. 👇
a = str(input("Enter the country: "))
b = str(input("Enter the cities: "))
c = int(input("Enter the number of visits: "))


def add_new_country(country_visited, cities_visited, visit_number):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = cities_visited
    new_country["visits"] = visit_number
    travel_log.append(new_country)


add_new_country(country_visited=a, cities_visited=b, visit_number=c)
print(travel_log)
