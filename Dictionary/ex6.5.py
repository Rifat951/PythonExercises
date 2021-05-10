# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through One key-value pair might be 'nile': 'egypt'
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt
# •	 Use a loop to print the name of each river included in the dictionary
# •	 Use a loop to print the name of each country included in the dictionary

print("\n\n")
print("####################")
print("\n\n")
rivers = {
    "nile" : "egypt",
    "padma" : "india",
    "the_other_padma": "bangladesh"
 }

for river_key, river_val in rivers.items():
    print("{} : {}".format(river_key,river_val))
