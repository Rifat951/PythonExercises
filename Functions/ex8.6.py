
# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned



def describe_city(city, country):
    a = print('"{}", "{}"'.format(city,country))
    return  a

city_name = input("enter the name of city.. \n")
country_name = input("enter the name of Country.. \n")

print("\n")
describe_city(city_name,country_name)